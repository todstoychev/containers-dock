import datetime


class Container:
    def __init__(self, container_id='', name='', status='', image='', command=None, ports=None, created=None):
        if ports is None:
            ports = {}
        if command is None:
            command = []
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
        string = ''

        if type(self.__command).__name__ != 'NoneType':
            return string

        for c in self.__command:
            string += ' ' + c

        return string

    @command.setter
    def command(self, value: list):
        self.__command = value

    @property
    def ports(self):
        ports = ''

        for p in list(self.__ports.keys()):
            ports += ' ' + p

        return ports

    @ports.setter
    def ports(self, value: dict):
        self.__ports = value

    @property
    def created(self):
        return self.__created

    @created.setter
    def created(self, value: datetime):
        self.__created = value
