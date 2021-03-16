from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QCheckBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread
from PyQt5.Qt import QColor, QPalette
import os
import mcpi
from PyQt5 import uic
import win32api
import win32gui
import win32con
import time
from pywinauto import Desktop

import logging


log = logging.getLogger(__name__)

spawnerViewUiPath = os.path.dirname(os.path.realpath(__file__)) + "\\spawnerViewUi.ui"
Ui_spawnerView, QtBaseClass = uic.loadUiType(spawnerViewUiPath)


class SpawnerView(QWidget, Ui_spawnerView):
    s_data_changed = pyqtSignal(dict)
    s_data_acquisition_done = pyqtSignal()

    # Initializing Functions

    def __init__(self, model=None, controller=None):
        super(SpawnerView, self).__init__()
        self.model = model
        self.setupUi(self)
        self.windowslist = []
        self.windows = Desktop(backend="uia").windows()

    def getWindowName(self):
        windows = Desktop(backend="uia").windows()
        for w in windows:
            self.windowslist.append(w.window_text())
        self.windowtitle = str([s for s in self.windowslist if "Minecraft*" in s][0])

    def actionInWindow(self, time):
        hWnd = win32gui.FindWindow(None, self.windowtitle)
        lParam = win32api.MAKELONG(50, 50)
        win32gui.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        time.sleep(time)
        win32gui.SendMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)
