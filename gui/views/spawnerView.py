from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QCheckBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread
from PyQt5.Qt import QColor, QPalette
import os
import mcpi
from PyQt5 import uic
import pythoncom
import win32api
import win32gui
import win32con
import win32com
import time
from pywinauto import Desktop
from threadWorker import Worker

import logging


log = logging.getLogger(__name__)

spawnerViewUiPath = os.path.dirname(os.path.realpath(__file__)) + "\\spawnerViewUi.ui"
Ui_spawnerView, QtBaseClass = uic.loadUiType(spawnerViewUiPath)


class SpawnerView(QWidget, Ui_spawnerView):

    def __init__(self, model=None, controller=None):
        super(SpawnerView, self).__init__()
        self.model = model
        self.setupUi(self)
        self.controllerThread = QThread()
        self.spawnWorker = None
        self.create_threads()
        self.connect_buttons()
        self.findWindow(50, 50)

    def connect_buttons(self):
        self.start.clicked.connect(self.controllerThread.run())
        self.stop.clicked.connect(self.stopSpawner)
        self.HWRange.valueChanged.connect(lambda: self.changeHWRange(self.HWRange.value()))
        self.SHRange.valueChanged.connect(lambda: self.changeSHRange(self.SHRange.value()))


    def create_threads(self, *args):
        pythoncom.CoInitialize()
        self.spawnWorker = Worker(self.startSpawner, *args)
        self.spawnWorker.moveToThread(self.controllerThread)
        self.controllerThread.started.connect(self.spawnWorker.run)


    def changeSHRange(self, shr):
        self.SHRangeValue = int(shr)


    def changeHWRange(self, hwr):
        self.HWRangeValue = int(hwr)


    def startSpawner(self, *args):
        pythoncom.CoInitialize()
        xl = win32com.client.Dispatch(
            pythoncom.CoGetInterfaceAndReleaseStream(self.hWnd, pythoncom.IID_IDispatch)
        )
        self.startStatus = True
        print(self.HWRange)
        while self.startStatus is True:
            self.clickWindow()
            time.sleep(int(self.HWRangeValue*60))


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

    def clickWindow(self):
        win32gui.SendMessage(self.hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, self.lParam)
        win32gui.SendMessage(self.hWnd, win32con.WM_LBUTTONUP, None, self.lParam)
        time.sleep(self.SHRangeValue)
        win32gui.SendMessage(self.hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, self.lParam)
        win32gui.SendMessage(self.hWnd, win32con.WM_LBUTTONUP, None, self.lParam)
        time.sleep(self.SHRangeValue)
        win32gui.SendMessage(self.hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, self.lParam)
        win32gui.SendMessage(self.hWnd, win32con.WM_LBUTTONUP, None, self.lParam)