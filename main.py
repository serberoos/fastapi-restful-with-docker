"""
Project Structure
Frontend - Jinja2 templates
FastAPI server - City(name,timezone)
CityModify(id,name,timezone)
PUT - id와 index 매칭
Database - Python list
"""
from fastapi import FastAPI
from pydantic import BaseModel

import requests

app = FastAPI()

db = []

class City(BaseModel):
    name: str
    timezone: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/cities') # GET
def get_cities(): # 모든 city 값 조회하기
    results = [] # 조회된 값 리스트
    for city in db: # db에서 city값을 하나씩 꺼낸다.
        str = f"http://worldtimeapi.org/api/timezone/{city['timezone']}" # api url에 timezone을 붙여서 url을 완성한다.
        print(str)
        r = requests.get(str) # 생성된 url을 이용해 api를 가져온다.
        cur_time = r.json()['datetime'] # 가져와진 r을 json화 하고 cur_time에 담는다.
        results.append({'name':city['name'], 'timezone':city['timezone'], 'current_time': cur_time})

    return results # 만들어진 city들을 담아서 돌려준다.


@app.get('/cities/{city_id}')
def get_city(city_id: int): # 디테일하게 city id를 이용해 조회
    city = db[city_id-1] # DB와 LIST 인덱스 맞추기
    r = requests.get(f"http://worldtimeapi.org/api/timezone/{city['timezone']}") #city의 timezone값을 넣는다.
    cur_time = r.json()['datetime'] # 가져와진 r을 json화 하고 cur_time에 담는다.
    return {'name':city['name'], 'timezone':city['timezone'], 'current_time': cur_time}


@app.post('/cities') #UPDATE CITY
def create_city(city: City):
    db.append(city.dict()) # 입력된 city를 딕셔너리로 바꿔서 넣어준다.
    return db[-1]


@app.delete('/cities/{city_id}') #DELETE city
def delete_city(city_id: int):
    db.pop(city_id-1) #LIST DB의 인덱스에 있는 값을 pop 한다.
    return {}




