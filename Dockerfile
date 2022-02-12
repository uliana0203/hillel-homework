FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-dev
COPY ./requirements.txt /flask_app/requirements.txt
WORKDIR /flask_app
RUN pip install -r requirements.txt
COPY . /flask_app
ENTRYPOINT ["python3"]
CMD ["flask_app.py"]