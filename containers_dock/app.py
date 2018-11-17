"""
Main application classes. Used to initialize the application.
"""
import sys

import docker
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from signal_dispatcher.signal_dispatcher import SignalDispatcher

from containers_dock.components import Containers
from containers_dock.controllers import ContainersController
from containers_dock.mappers import ContainerMapper
from containers_dock.threads import EventsThread
from containers_dock.utils import Config


class App:
    def __init__(self):
        self.__config = Config()
        self.__app = QApplication(sys.argv)
        self.__main_widget = Containers()
        self.__client = docker.from_env()
        self.__container_mapper = ContainerMapper()
        self.__containers_controller = ContainersController(
            self.__client,
            self.__container_mapper,
            self.__main_widget.table,
            self.__main_widget.show_all,
        )

    def run(self):
        title = self.__config.get('app.name') + ' v.' + self.__config.get('app.version')
        self.__main_widget.setWindowTitle(title)
        self.__main_widget.setWindowIcon(QIcon(self.__config.get('app.icon')))
        self.__main_widget.build()
        self.__containers_controller.list()
        self.__main_widget.showMaximized()

        events = EventsThread(client=self.__client)
        events.start()
        events.refresh_list.connect(self.__containers_controller.list)

        SignalDispatcher.dispatch()

        self.__app.exec()

    @property
    def client(self):
        return self.__client
