import json

from PyQt5.QtCore import QThread, pyqtSignal
from docker import DockerClient


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
