
from PyQt5.QtCore import Qt, QAbstractTableModel, QObject
import json
from PyQt5.QtWidgets import QTableView, QSizePolicy, QHeaderView, QWidget, QItemDelegate, QPushButton, QAbstractItemView, QComboBox
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QModelIndex, QAbstractItemModel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QIcon
import os
import logging


log = logging.getLogger(__name__)


class ParametersTableModel(QAbstractTableModel):
    s_data_changed = pyqtSignal()

    def __init__(self):
        super(ParametersTableModel, self).__init__()


class ParametersTableView(QWidget):
    def __init__(self, parent, table_model):
        super(ParametersTableView, self).__init__()
        self.parent = parent
        self.table_view = QTableView(self.parent)
        self.table_model = table_model
        self.table_view.setModel(self.table_model)
        self.setup_table_visuals()
        self.table_view.clicked.connect(self.get_selected_index_on_click)

    def load_data(self, jsonData):
        for parameter in jsonData['[all]'].keys():
            a = [""]
            a.append(parameter)
            for i in range(2):
                try:
                    a.append(jsonData['[all]'][parameter]["p{}".format(i+1)])
                except Exception:
                    a.append("")
            self.add_data_row(a)