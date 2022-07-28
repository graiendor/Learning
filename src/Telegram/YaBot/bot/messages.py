import abc

import telegram as tg
import telegram.ext as tg_ext


class BaseMessages(abc.ABC):
    @abc.abstractmethod
    def start(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def help(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def echo(self, text: str) -> str:
        raise NotImplemented


class RegularUsers(BaseMessages):
    def start(self) -> str:
        return 'Hi!'

    def help(self) -> str:
        return 'Buy subscription'

    def echo(self, text: str) -> str:
        return f'{text}'


class PremiumUsers(RegularUsers):
    def start(self) -> str:
        return 'Hi!'

    def help(self) -> str:
        return 'Well bought'


def getMessages(user: tg.User) -> BaseMessages:
    if user.is_premium:
        return PremiumUsers()
    else:
        return RegularUsers()
