"""
Qt components classes
"""

import qtawesome
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QToolBar, QAction, QTableWidget, QTableWidgetItem, QAbstractItemView, \
    QCheckBox


class Containers(QWidget):
    """
    Containers QtWidget.

    Attributes:
        :__layout (QVBoxLayout):
        :__toolbar (Toolbar):
    """

    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)
        self.__layout = QVBoxLayout()
        self.__toolbar = Toolbar()
        self.__table = Table()
        self.__show_all = ShowAll()

    def build(self):
        """
        Builds the interface.
        :return:
        """
        self.__layout.setMenuBar(self.__toolbar)
        self.__toolbar.build()

        self.__layout.addWidget(self.__table)
        self.__table.build()

        self.__layout.addWidget(self.__show_all)

        self.setLayout(self.__layout)

    @property
    def toolbar(self):
        return self.__toolbar

    @property
    def table(self):
        return self.__table

    @property
    def show_all(self):
        return self.__show_all


class Toolbar(QToolBar):
    """
    Containers window toolbar.

    Attributes:
        :__start_action (QAction):
        :__stop_action (QAction):
        :__restart_action (QAction):
        :__delete_action (QAction):
        :__terminal_action (QAction):
    """

    def __init__(self, *__args):
        super().__init__(*__args)
        self.__start_action = QAction(qtawesome.icon('fa.play'), 'Start', self)
        self.__stop_action = QAction(qtawesome.icon('fa.stop'), 'Stop', self)
        self.__restart_action = QAction(qtawesome.icon('fa.refresh'), 'Restart', self)
        self.__remove_action = QAction(qtawesome.icon('fa.trash'), 'Delete', self)
        self.__terminal_action = QAction(qtawesome.icon('fa.terminal'), 'Terminal', self)
        self.__show_all = QCheckBox('Show all')

    def build(self):
        # Start action
        self.__start_action.setToolTip('Start container')
        self.addAction(self.__start_action)

        # Stop action
        self.__stop_action.setToolTip('Stops running containers.')
        self.addAction(self.__stop_action)

        # Restart action
        self.__restart_action.setToolTip('Restart containers.')
        self.addAction(self.__restart_action)

        # Delete action
        self.__remove_action.setToolTip('Force deletes container.')
        self.addAction(self.__remove_action)

        # Terminal action
        self.__terminal_action.setToolTip('Open terminal session to containers.')
        self.addAction(self.__terminal_action)

    @property
    def start_action(self):
        return self.__start_action

    @property
    def stop_action(self):
        return self.__stop_action

    @property
    def restart_action(self):
        return self.__restart_action

    @property
    def remove_action(self):
        return self.__remove_action

    @property
    def terminal_action(self):
        return self.__terminal_action


class Table(QTableWidget):
    """
    Attributes:
       __columns (list): Column labels.
    """

    COLUMN_NAMES = ["ID", "Status", "Name", "Image", "Command", "Ports", "Created"]

    def __init__(self, *__args):
        super().__init__(*__args)

    def build(self):
        columns = self.COLUMN_NAMES
        self.setColumnCount(columns.__len__())
        self.setSortingEnabled(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def set_row_data(self, data: list, row: int):
        """
        Adds data to table row.

        :param data: Data to add.
        :param row: Row number.
        :return:
        """
        index = 0

        for item in data:
            self.setItem(row, index, QTableWidgetItem(item))
            index += 1

        self.resizeColumnsToContents()
        columns = self.COLUMN_NAMES
        self.setHorizontalHeaderLabels(columns)

    def get_selected_items(self, column_number: int):
        """
        Gets selected items identificators, using column number to point to the identification data.

        :param column_number: Column number, where object identificators is.
        :return (list): List of identificators.
        """
        selection = self.selectedItems()
        items = []

        for item in selection:
            if item.column() is column_number:
                items.append(item.text())

        return items


class ShowAll(QCheckBox):
    """
    Show all containers checkbox.
    """

    def __init__(self, *__args):
        super().__init__(*__args)
        self.setText('Show all')
        self.setToolTip('Displays stopped containers if checked.')
