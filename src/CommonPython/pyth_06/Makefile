all: build

build:
	bash start.sh
	docker-compose build
	docker-compose up

down:
	docker-compose down

clean:
	rm -rf store/store_pb2.py
	rm -rf store/store_pb2_grpc.py
	rm -rf input/input_pb2.py
	rm -rf input/input_pb2_grpc.py
	rm -rf json/json_pb2.py
	rm -rf json/json_pb2_grpc.py

	rm -rf api/store_pb2.py
	rm -rf api/store_pb2_grpc.py
	rm -rf api/input_pb2.py
	rm -rf api/input_pb2_grpc.py
	rm -rf api/json_pb2.py
	rm -rf api/json_pb2_grpc.py