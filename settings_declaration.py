from settings_dataclasses import BaseSettingObject


class MDMIP(BaseSettingObject):
    def get_setting(self):
        return '127.0.0.1'


class MDMPort(BaseSettingObject):
    def get_setting(self):
        return 5432
