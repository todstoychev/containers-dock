"""
Main application classes. Used to initialize the application.
"""
import sys

import docker
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from containers_dock.components import Containers
from containers_dock.controllers import ContainersController
from containers_dock.mappers import ContainerMapper
from containers_dock.threads import EventsThread


class App:
    APP_NAME = "Containers dock"
    VERSION = "0.1.5"
    ICON = "resources/icon.png"

    def __init__(self):
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
        title = self.APP_NAME + ' v.' + self.VERSION
        self.__main_widget.setWindowTitle(title)
        self.__main_widget.setWindowIcon(QIcon(self.ICON))
        self.__main_widget.build()
        self.__containers_controller.list()
        self.__main_widget.showMaximized()

        # Mapping actions
        self.__main_widget.toolbar.stop_action.triggered.connect(self.__containers_controller.stop_containers)
        self.__main_widget.toolbar.start_action.triggered.connect(self.__containers_controller.start_containers)
        self.__main_widget.toolbar.restart_action.triggered.connect(self.__containers_controller.restart_containers)
        self.__main_widget.toolbar.remove_action.triggered.connect(self.__containers_controller.remove_containers)
        self.__main_widget.toolbar.terminal_action.triggered.connect(self.__containers_controller.open_terminal)
        self.__main_widget.show_all.clicked.connect(self.__containers_controller.toggle_show_all)

        events = EventsThread(client=self.__client)
        events.start()
        events.refresh_list.connect(self.__containers_controller.list)

        self.__app.exec()

    @property
    def client(self):
        return self.__client
