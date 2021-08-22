# Practice barisori's fastapi basic lecture and build a docker container
lecture Link : https://www.youtube.com/watch?v=7frN5JPMsQU

* **Dockerfile content**

  FROM python:3.7

  RUN pip install fastapi
  RUN pip install uvicorn
  RUN pip install requests
  RUN pip install jinja2

  EXPOSE 80

  COPY ./app /app
  COPY ./templates /templates
  COPY ./\_\_pycache\_\_ /\_\_pycache\_\_
  COPY ./.idea /.idea

  CMD ["uvicorn","app.mainlist:app","--host","0.0.0.0","--port","80"]
  

* **How use it?**

  Open terminal and typing!
  
  **docker run --rm --name fastapi_docker_practice -p 12332:80 fastapi_docker_practice:first**

