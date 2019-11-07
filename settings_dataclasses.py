import datetime
from abc import abstractmethod

from dataclasses import dataclass
from typing import TypeVar, Type, Union


class BaseSettingObject(object):

    def __init__(self, name, expire):
        self.name = name
        self.expire = expire
        self._value = None
        self.last_update = None

    def __hash__(self):
        return hash(self.name)

    def check_update_required(self):
        if self.expire is not None:
            if self.last_update is None:
                return True
            if datetime.datetime.now() > self.last_update + datetime.timedelta(minutes=self.expire):
                return True
        return False

    def update_value(self):
        if self._value is None:
            self._value = self.get_setting()
            self.last_update = datetime.datetime.now()
        else:
            if self.check_update_required():
                self._value = self.get_setting()
                self.last_update = datetime.datetime.now()

    @property
    def value(self):
        self.update_value()
        return self._value

    @abstractmethod
    def get_setting(self):
        return 'Метод для получения настройки, должен возвращать настройку'


BSO = TypeVar('BSO', bound=BaseSettingObject)


@dataclass
class SettingListElement:
    """
    Класс для описание списка настроек по указанному шаблону

    :param name: Имя
    :param cls: Класс-контроллер наследник BaseSettingObject
    :param expire: "время жизни" параметра в минутах. | None - не обновляется
    """
    name: str
    cls: Type[BSO]
    expire: Union[int, None]
