# -*- coding: utf-8 -*-
import random
import time
from threading import Thread

from settings_classes import Settings


class TestThread(Thread):
    """
    A threading example
    """

    def __init__(self, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
        self.config = Settings()

    def run(self):
        """Запуск потока"""
        amount = random.randint(3, 15)
        time.sleep(amount)
        msg = f"{self.name} is running. Settings is: {self.config['ip']}:{self.config['port']}"
        print(msg)


def create_threads():
    """
    Создаем группу потоков
    """
    for i in range(5):
        name = "Thread #%s" % (i + 1)
        my_thread = TestThread(name)
        my_thread.start()


if __name__ == "__main__":
    create_threads()
