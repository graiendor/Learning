#!/bin/bash

mkdir -p store
mkdir -p input
mkdir -p json_serv

python3 -m grpc_tools.protoc -I=./proto --python_out=./json_serv --grpc_python_out=./json_serv ./proto/json.proto
python3 -m grpc_tools.protoc -I=./proto --python_out=./api --grpc_python_out=./api ./proto/json.proto
python3 -m grpc_tools.protoc -I=./proto --python_out=./input --grpc_python_out=./input ./proto/input.proto
python3 -m grpc_tools.protoc -I=./proto --python_out=./api --grpc_python_out=./api ./proto/input.proto
python3 -m grpc_tools.protoc -I=./proto --python_out=./store --grpc_python_out=./store ./proto/store.proto
python3 -m grpc_tools.protoc -I=./proto --python_out=./api --grpc_python_out=./api ./proto/store.proto