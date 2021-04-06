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


    def connect_buttons(self):
        self.start.clicked.connect(self.startSpawner(self.HWRange, self.SHRange))
        self.stop.clicked.connect(self.stopSpawner())


    def startSpawner(self, HWR, SHR):
        self.findWindow(50, 50)
        self.startStatus = True
        while self.startStatus is True:
            self.clickWindow(SHR)
            time.sleep(HWR*60)


    def stopSpawner(self):
        self.startStatus = False


    def resetSpawner(self):
        self.stopSpawner()
        self.HWRange = 0.00
        self.SHRange = 0,00


    def findWindow(self, x, y):
        windowslist = []
        windows = Desktop(backend="uia").windows()
        for w in windows:
            windowslist.append(w.window_text())
        windowtitle = str([s for s in windowslist if "Minecraft*" in s][0])
        print(f"fWindow found: {windowtitle}")

        self.hWnd = win32gui.FindWindow(None, windowtitle)
        self.lParam = win32api.MAKELONG(x, y)

    def clickWindow(self, SHR):
        win32gui.SendMessage(self.hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, self.lParam)
        time.sleep(SHR)
        win32gui.SendMessage(self.hWnd, win32con.WM_LBUTTONUP, None, self.lParam)
