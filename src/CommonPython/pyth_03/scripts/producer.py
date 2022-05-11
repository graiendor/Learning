import json

import redis
from time import sleep
from json import dumps


def stream():
    """Produces a json data, which consists of the sender and receiver (10 digits id) and the amount of transfered money.
    Then publishes it to the channel"""
    publisher.subscribe('bad guyz')
    while True:
        sleep(3)
        sender = 1056
        receiver = 1024
        money = 1000
        guy = {'metadata': {'from': sender, 'to': receiver}, 'amount': money}

        server.publish('bad guyz', json.dumps(guy))


if __name__ == '__main__':
    server = redis.Redis(host='localhost', port=6379, db=0)
    publisher = server.pubsub()
    stream()
