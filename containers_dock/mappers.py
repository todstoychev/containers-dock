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
        command = ContainerMapper.__parse_cmd(config.get('Cmd'))

        return Model(
            container_id=container.short_id,
            status=container.status,
            name=container.name,
            image=config.get('Image'),
            command=command,
            ports=ContainerMapper.__parse_ports(container.attrs.get('NetworkSettings').get('Ports')),
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

    @staticmethod
    def __parse_ports(ports: dict):
        """

            parsed += port        :param ports:  Ports mappings
        :return: Ports string
        """
        if ports is None or ports.__len__() == 0:
            return ''

        parsed = ''
        keys = sorted(ports.keys())

        for port in keys:
            if ports.get(port) is not None:
                mappings = ports.get(port)

                for mapping in mappings:
                    parsed += mapping.get('HostIp') + ':' + mapping.get('HostPort') + '->' + port

                    if mapping.get('HostPort') != mappings[-1].get('HostPort') or port != keys[-1]:
                        parsed += ', '

                if port != keys[-1]:
                    parsed += ', '

        return parsed

