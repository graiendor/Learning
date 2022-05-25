import json_server
import json_pb2_grpc
import json_pb2
import grpc
import json
from pytest import raises
import os
import shutil

service = json_server.JsonService()

channel = grpc.insecure_channel('localhost:8092')
stub = json_pb2_grpc.ProcessJsonStub(channel)
