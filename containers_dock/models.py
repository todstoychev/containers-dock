import datetime


class Container:
    def __init__(self, container_id='', name='', status='', image='', command='', ports=None, created=None):
        if ports is None:
            ports = {}

        self.__id = container_id
        self.__name = name
        self.__status = status
        self.__image = image
        self.__command = command
        self.__ports = ports
        self.__created = created

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value: str):
        self.__status = value

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value: str):
        self.__image = value

    @property
    def command(self):
        return self.__command

    @command.setter
    def command(self, value: list):
        self.__command = value

    @property
    def ports(self):
        return self.__ports

    @ports.setter
    def ports(self, value: dict):
        self.__ports = value

    @property
    def created(self):
        return self.__created

    @created.setter
    def created(self, value: datetime):
        self.__created = value
