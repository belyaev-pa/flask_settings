from settings_dataclasses import SettingListElement
from settings_declaration import MDMIP, MDMPort


SETTINGS_LIST = [
    SettingListElement(name='ip', cls=MDMIP, expire=10),
    SettingListElement(name='port', cls=MDMPort, expire=10)
]


