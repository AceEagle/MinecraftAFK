from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QModelIndex, Qt, QAbstractItemModel
from pyqtgraph import PlotItem, BarGraphItem
from gui.widgets.parametersTableWidget import ParametersTableModel
from gui.widgets.parametersTableWidget import ParametersTableView
from PyQt5 import uic, QtCore
from scipy.stats import binom, geom, dlaplace, logser, nbinom, poisson, planck, randint, zipf
import numpy as np
import logging
import json
import time
import os

log = logging.getLogger(__name__)

fishingViewUiPath = os.path.dirname(os.path.realpath(__file__)) + '\\fishingUi.ui'
Ui_fishingView, QtBaseClass = uic.loadUiType(fishingViewUiPath)


class FishingView(QWidget, Ui_fishingView):  # type: QWidget

    s_lens_data_changed = pyqtSignal(dict)

    def __init__(self, model=None, controller=None):
        super(FishingView, self).__init__()
        self.setupUi(self)
        self.model = model
        self.plotItem = None
        self.dataPlotItem = None
        self.connect_widgets()
        self.create_plots()