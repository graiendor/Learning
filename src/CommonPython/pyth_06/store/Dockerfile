FROM python:3.6.14

RUN mkdir -p /usr/src/app/ ; mkdir -p /usr/src/app/proto ; mkdir -p /usr/src/app/subjects
WORKDIR /usr/src/app/

COPY store/__init__.py /usr/src/app/
COPY store/store_server.py /usr/src/app/
COPY proto/store.proto /usr/src/app/proto
COPY requirements.txt  /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8093

USER root

RUN python -m grpc_tools.protoc -I=./proto --python_out=. --grpc_python_out=. ./proto/store.proto
CMD ["python", "store_server.py"]