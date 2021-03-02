from gui.dialog.helpDialog import HelpDialog
from gui.views.spawnerView import SpawnerView
from gui.views.fishingView import FishingView
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QTabWidget, QAction, QApplication
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
import logging
import os
from PyQt5 import uic


log = logging.getLogger(__name__)


MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '\\mainWindowUi.ui'
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, model=None, controller=None):
        super(MainWindow, self).__init__()
        self.setAttribute(Qt.WA_AlwaysStackOnTop)
        self.setupUi(self)
        self.model = model

        self.create_views_and_dialogs()
        self.setup_window_tabs()
        self.setup_statusBar()
        self.setup_menuBar()
        self.connect_buttons()
        self.connect_signals()

    def setup_window_tabs(self):
        self.tabWidget = QTabWidget()
        self.setCentralWidget(self.tabWidget)
        self.tabWidget.addTab(self.spawnerView, "Spawner")
        self.tabWidget.addTab(self.fishingView, "Fishing")

    def setup_menuBar(self):
        self.helpAction = QAction(self)
        self.helpAction.setText("Help")
        self.menubar.addAction(self.helpAction)

    def setup_statusBar(self):
        self.statusbarMessage = QLabel()
        self.statusbar.addWidget(self.statusbarMessage)

    def create_views_and_dialogs(self):
        self.helpDialog = HelpDialog()
        self.spawnerView = SpawnerView(model=self.model)
        self.fishingView = FishingView(model=self.model)