from weakref import WeakValueDictionary

from settings_list import SETTINGS_LIST


class Singleton(type):
    _instances = WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Settings(object, metaclass=Singleton):
    settings_list = SETTINGS_LIST
    cache = dict()
    set_error = 'You can`t set settings by yourself. Use declaration classes'

    def __init__(self):
        self.load_settings_names()

    def __getitem__(self, key):
        return self._get_value(key)

    def __getattr__(self, name):
        return self._get_value(name)

    def __setitem__(self, key, value):
        raise NotImplementedError(self.set_error)

    def __setattr__(self, key, value):
        raise NotImplementedError(self.set_error)

    def __len__(self):
        return len(self.cache.keys())

    def _get_value(self, key):
        try:
            item = self.cache[key]
        except KeyError:
            NotImplementedError(f'No {key} settings found. Use declaration classes')
        else:
            return item.value

    def load_settings_names(self):
        for obj in self.settings_list:
            self.cache[obj.name] = obj.cls(name=obj.name, expire=obj.expire)
