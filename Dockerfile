# Dockerfile

# pull the official docker image
FROM python:3.7

RUN mkdir /fastapi
COPY requirements.txt /fastapi

# set work directory
WORKDIR /fastapi

# install dependencies
RUN pip install -r requirements.txt

COPY . /fastapi

EXPOSE 8000

CMD ["uvicorn","app.mainlist:app","--host","0.0.0.0","--port","8000"]