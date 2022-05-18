FROM python:3.6.14

RUN mkdir -p /usr/src/app/ ; mkdir -p /usr/src/app/proto
WORKDIR /usr/src/app/

COPY input/__init__.py /usr/src/app/
COPY input/input_server.py /usr/src/app/
COPY proto/input.proto /usr/src/app/proto
COPY requirements.txt  /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8091

USER root

RUN python -m grpc_tools.protoc -I=./proto --python_out=. --grpc_python_out=. ./proto/input.proto
CMD ["python", "input_server.py"]