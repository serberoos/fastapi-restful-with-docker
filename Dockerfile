FROM python:3.7

RUN pip install fastapi
RUN pip install uvicorn
RUN pip install requests
RUN pip install jinja2

EXPOSE 80

COPY ./app /app
COPY ./templates /templates
COPY ./__pycache__ /__pycache__
COPY ./.idea /.idea

CMD ["uvicorn","app.mainlist:app","--host","0.0.0.0","--port","80"]