import json
import random

import redis
from time import sleep


def stream():
    """Produces a json data, which consists of the sender and receiver (10 digits id) and the amount of transfered money.
    Then publishes it to the channel"""
    publisher.subscribe('bad guyz')
    while True:
        sleep(3)
        send_guyz: list = [4444444444, 1111111111, 2222222222, 3333333333, 5555555555, 6666666666]
        receive_guyz: list = [2444444444, 3111111111, 3222222222, 2333333333, 3555555555, 2666666666]
        sender = random.choice(send_guyz)
        receiver = random.choice(receive_guyz)
        money = random.randrange(-10000, 10000, 1100)
        # guy = {'metadata': {'from': sender, 'to': receiver}, 'amount': money}
        guy = {'metadata': {'from': sender, 'to': 4444444444}, 'amount': money}

        server.publish('bad guyz', json.dumps(guy))


if __name__ == '__main__':
    server = redis.Redis(host='localhost', port=6379, db=0)
    publisher = server.pubsub()
    stream()
