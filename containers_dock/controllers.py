import subprocess
from multiprocessing import Process

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from docker import DockerClient

from containers_dock.components import Table, ShowAll
from containers_dock.mappers import ContainerMapper


class ContainersController:
    def __init__(self, client: DockerClient, container_mapper: ContainerMapper, table: Table, show_all: ShowAll):
        self.__client = client
        self.__mapper = container_mapper
        self.__table = table
        self.__show_all = show_all

    def list(self):
        """
        Lists container data and sets up the table.

        :return:
        """

        QApplication.instance().setOverrideCursor(Qt.BusyCursor)
        containers = self.__client.containers.list(self.__show_all.isChecked())
        self.__table.clear()
        self.__table.setRowCount(0)
        self.__table.setRowCount(containers.__len__())
        row = 0

        for container in containers:
            model = self.__mapper.map(container)

            self.__table.set_row_data([
                model.id,
                model.status,
                model.name,
                model.image,
                model.command,
                model.ports,
                model.created.strftime("%d %b %Y - %I:%m:%S")
            ], row)
            row += 1

        QApplication.instance().restoreOverrideCursor()

    def stop_containers(self):
        QApplication.instance().setOverrideCursor(Qt.BusyCursor)
        containers = self.__table.get_selected_items(0)

        for container in containers:
            self.__client.containers.get(container).stop()

        QApplication.instance().restoreOverrideCursor()

    def start_containers(self):
        QApplication.instance().setOverrideCursor(Qt.BusyCursor)
        containers = self.__table.get_selected_items(0)

        for container in containers:
            self.__client.containers.get(container).start()

        QApplication.instance().restoreOverrideCursor()

    def restart_containers(self):
        QApplication.instance().setOverrideCursor(Qt.BusyCursor)
        containers = self.__table.get_selected_items(0)

        for container in containers:
            self.__client.containers.get(container).restart()

        # self.list(self.__show_all.isChecked())
        QApplication.instance().restoreOverrideCursor()

    def remove_containers(self):
        QApplication.instance().setOverrideCursor(Qt.BusyCursor)
        containers = self.__table.get_selected_items(0)

        for container in containers:
            self.__client.containers.get(container).remove(force=True)

        # self.list(self.__show_all.isChecked())
        QApplication.instance().restoreOverrideCursor()

    def open_terminal(self):
        QApplication.instance().setOverrideCursor(Qt.BusyCursor)
        containers = self.__table.get_selected_items(0)

        for container in containers:
            command = subprocess.Popen(['x-terminal-emulator', '-e', 'docker', 'exec', '-it', container, 'sh'])
            p = Process(target=command)
            p.start()

        # self.list(self.__show_all.isChecked())
        QApplication.instance().restoreOverrideCursor()

    def toggle_show_all(self):
        self.list()
