FROM python:3.6.14

RUN mkdir -p /usr/src/app/ ; mkdir -p /usr/src/app/proto
WORKDIR /usr/src/app/

COPY json_serv/__init__.py /usr/src/app/
COPY json_serv/json_server.py /usr/src/app/
COPY json_serv/QA.json /usr/src/app/
COPY proto/json.proto /usr/src/app/proto
COPY requirements.txt  /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8092

USER root

RUN python -m grpc_tools.protoc -I=./proto --python_out=. --grpc_python_out=. ./proto/json.proto
CMD ["python", "json_server.py"]