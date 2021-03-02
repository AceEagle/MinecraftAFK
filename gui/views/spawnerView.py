from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QCheckBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread
from PyQt5.Qt import QColor, QPalette
import os
import mcpi
from PyQt5 import uic


import logging


log = logging.getLogger(__name__)

spawnerViewUiPath = os.path.dirname(os.path.realpath(__file__)) + "\\spawnerUi.ui"
Ui_spawnerView, QtBaseClass = uic.loadUiType(spawnerViewUiPath)


class SpawnerView(QWidget, Ui_spawnerView):
    s_data_changed = pyqtSignal(dict)
    s_data_acquisition_done = pyqtSignal()

    # Initializing Functions

    def __init__(self, model=None, controller=None):
        super(SpawnerView, self).__init__()
        self.model = model
        self.setupUi(self)

    def