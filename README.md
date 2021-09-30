# Implementation of fastapi RESTful API with docker container and docker compose

* **Dockerfile content**

  * Docker repository : https://hub.docker.com/repository/docker/jae99c/fastapi_docker_practice

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

  docker push jae99c/fastapi_docker_practice:first

  docker run --rm --name fastapi_docker_practice -p **[client_port_num]**:80 jae99c/fastapi_docker_practice:first
  
* **Reference**

  https://www.youtube.com/watch?v=7frN5JPMsQU
