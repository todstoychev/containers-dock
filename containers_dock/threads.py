import json

from PyQt5.QtCore import QThread, pyqtSignal
from docker import DockerClient
from docker.models.containers import Container

from containers_dock.components import Logs


class EventsThread(QThread):
    """
    EventsThread is used to emit events on containers operations detected. This keeps the interface up to date with
    the changes behind.

    Attributes:
        :client (DockerClient): Docker client
        :refresh_list (pyqtSignal): Signal that is emitted
    """
    refresh_list = pyqtSignal()

    def __init__(self, client: DockerClient):
        """
        :param client (DockerClient):
        """
        super().__init__()
        self.client = client

    def run(self):
        events = self.client.events()

        for event in events:
            event = json.loads(event.decode('utf-8'))

            if event['Type'] == 'container':
                self.refresh_list.emit()
                pass


class LogsThread(QThread):
    """
    LogsThread is used to start new Logs widget.

    Attributes:
        :logs_line (pyqtSignal):
        :__container (Container):
    """
    logs_line = pyqtSignal([str])

    def __init__(self, container: Container):
        """
        :param container:
        """
        super().__init__()
        self.container = container

    def run(self):
        for line in self.container.logs(stream=True):
            self.logs_line.emit(line.strip().decode('utf-8'))

        pass


