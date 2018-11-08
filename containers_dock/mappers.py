"""
Model mappers.
"""

from docker.models.containers import Container
from containers_dock.models import Container as Model
from datetime import datetime


class ContainerMapper:
    """
    Container model mapper.
    """

    @staticmethod
    def map(container: Container):
        config = container.attrs.get('Config')

        try:
            ports = config.get('ExposedPorts')
        except KeyError:
            ports = {}

        command = ContainerMapper.__parse_cmd(config.get('Cmd'))

        return Model(
            container_id=container.short_id,
            status=container.status,
            name=container.name,
            image=config.get('Image'),
            command=command,
            ports=ports,
            created=datetime.strptime(
                container.attrs['Created'][0:-7],
                '%Y-%m-%dT%H:%M:%S.%f')
        )

    @staticmethod
    def __parse_cmd(cmd: list):
        """
        :param cmd:
        :return: Command string
        """
        command = ''

        if type(cmd).__name__ == 'NoneType':
            return ''

        for c in cmd:
            command += c + ' '

        return command
