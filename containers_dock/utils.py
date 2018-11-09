import configparser
import os


class Config:
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self.__config = configparser.ConfigParser()
        self.__config.read(path + '/config.ini')
        self.__config.sections()

    def get(self, key):
        (section, value) = key.split('.')

        return self.__config[section][value]
