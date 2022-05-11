import redis

server = redis.StrictRedis('127.0.0.1', 6379, charset="utf-8", decode_responses=True)


def stream():
    server.publish('bad guyz', '43434')


if __name__ == '__main__':
    stream()
