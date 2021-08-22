"""
Project Structure
Frontend - Jinja2 templates
FastAPI server - City(name,timezone)
CityModify(id,name,timezone)
PUT - id와 index 매칭
Database - Python list

mainlist - 웹으로 표현하기
"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates  # Jinja는 파이썬에서 HTML을 표현하는 표준이다.

from pydantic import BaseModel

import requests

app = FastAPI()

db = []

# ----------------------------------------------------------
# Models
# ----------------------------------------------------------
class City(BaseModel):
    name: str
    timezone: str

class CityModify(BaseModel):
    id : int
    name: str
    timezone: str


templates = Jinja2Templates(directory="templates")  # fastapi_basic_practice_bipasori/templates 연결




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/cities', response_class=HTMLResponse)  # response_class는 HTMLResponse로 정의
def get_cities(request: Request):  # 모든 city 값 조회하기 | request에는 Request를 받는다.
    context = {} # 리턴할 것

    rsCity = []  # 조회된 값 리스트

    cnt = 0 # 조회 값이 append될 때마다 cnt값을 하나씩 증가시켜 index로 표시한다.

    for city in db:  # db에서 city값을 하나씩 꺼낸다.
        str = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"  # api url에 timezone을 붙여서 url을 완성한다.
        print(str)
        r = requests.get(str)  # 생성된 url을 이용해 api를 가져온다.
        cur_time = r.json()['datetime']  # 가져와진 r을 json화 하고 cur_time에 담는다.

        cnt += 1
        rsCity.append({'id': cnt, 'name': city['name'], 'timezone': city['timezone'], 'current_time': cur_time})

    # 리턴할 list context에는 request와 rsCity가 존재함
    context['request'] = request
    context['rsCity'] = rsCity

    return templates.TemplateResponse("city_list.html", context)  # city_list.html을 호출하고 웹화면이 그려진다.
    #city_list - html template
    #city_list_simple - simple template


@app.get('/cities/{city_id}', response_class=HTMLResponse)
def det_city(request: Request, city_id: int):  # 디테일하게 city id를 이용해 조회
    city = db[city_id-1]  # DB와 LIST 인덱스 맞추기
    r = requests.get(f"http://worldtimeapi.org/api/timezone/{city['timezone']}")  # city의 timezone값을 넣는다.
    cur_time = r.json()['datetime']  # 가져와진 r을 json화 하고 cur_time에 담는다.
    # return {'name': city['name'], 'timezone': city['timezone'], 'current_time': cur_time}
    context = {'request':request, 'name':city['name'], 'timezone':city['timezone'], 'current_time': cur_time}
    return templates.TemplateResponse("city_detail.html", context)


@app.post('/cities')  # CREATE CITY
def create_city(city: City):
    db.append(city.dict())  # 입력된 city를 딕셔너리로 바꿔서 넣어준다.
    return db[-1]

@app.put('/cities')  # UPDATE CITY
def modify_city(city: CityModify):
    db[city.id-1] = { 'name': city.name, 'timezone': city.timezone } # 수정
    return db[city.id-1] #수정된 값 리턴


@app.delete('/cities/{city_id}')  # DELETE city
def delete_city(city_id: int):
    db.pop(city_id-1)  # LIST DB의 인덱스에 있는 값을 pop 한다.
    return {'result_msg':'Deleted...'}
