import asyncio
import time

from enum import Enum, auto
from random import choice

start_time = time.time()

class Action(Enum):
    HIGHKICK = auto()
    LOWKICK = auto()
    HIGHBLOCK = auto()
    LOWBLOCK = auto()


class Agent:
    def __init__(self):
        self.__aiter__()

    def __aiter__(self, health=5):
        self.health = health
        self.actions = list(Action)
        return self

    async def __anext__(self):
        return choice(self.actions)

    async def act(self):
        return await self.__anext__()


class Neo:

    action = None

    async def fight(self):
        agents = [Agent() for _ in range(10)]

        while agents:
            index = choice([0, len(agents) - 1])
            agent = agents[index]
            reply = asyncio.create_task(self.reply(agent))
            agent_action = await reply
            if self.action == Action.LOWKICK or self.action == Action.HIGHKICK:
                agent = agent.__aiter__(agent.health - 1)
            print({'Agent': agent_action.name, 'Neo': self.action.name, 'Agent Health': agent.health})
            if agent.health == 0:
                agents.pop(index)
        print('Neo wins')
        print("--- %s seconds ---" % (time.time() - start_time))

    async def reply(self, agent):
        action = await agent.act()
        if action == Action.HIGHKICK:
            self.action = Action.HIGHBLOCK
        if action == Action.HIGHBLOCK:
            self.action = Action.LOWKICK
        if action == Action.LOWKICK:
            self.action = Action.LOWBLOCK
        if action == Action.LOWBLOCK:
            self.action = Action.HIGHKICK
        return action


if __name__ == "__main__":
    neo = Neo()
    asyncio.run(neo.fight())
