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
        try:
            ports = container.attrs['Config']['ExposedPorts']
        except KeyError:
            ports = {}

        return Model(
            container_id=container.short_id,
            status=container.status,
            name=container.name,
            image=container.image.tags[0],
            command=container.attrs['Config']['Cmd'],
            ports=ports,
            created=datetime.strptime(
                container.attrs['Created'][0:-7],
                '%Y-%m-%dT%H:%M:%S.%f')
        )
