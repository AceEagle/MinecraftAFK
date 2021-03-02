import numpy as np
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFontDatabase
from gui.windows.mainWindow import MainWindow
from mainModel import MainModel
import mcpi
import ctypes
import sys
import logging
import logging.config
from logging.handlers import RotatingFileHandler
import os

log = logging.getLogger(__name__)


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        sys.excepthook = self.handle_exception
        self.init_logging()
        log.debug("This is the MAIN THREAD")
        self.setAttribute(Qt.AA_EnableHighDpiScaling)
        QFontDatabase.addApplicationFont(
            os.path.dirname(os.path.realpath(__file__)) + "\\gui\\misc\\Open_Sans\\OpenSans-Light.ttf")
        self.setStyle("Fusion")
        # self.setStyleSheet(CSSThemes().orange_theme())
        self.mainModel = MainModel()
        self.mainWindow = MainWindow(model=self.mainModel)
        self.mainWindow.setWindowTitle("MinecraftAFK")
        self.mainWindow.show()

    @staticmethod
    def init_logging():
        logger = logging.getLogger()
        logger.setLevel(logging.NOTSET)

        # create console handler
        handler = logging.StreamHandler()
        handler.setLevel(logging.NOTSET)
        formatter = logging.Formatter(
            "%(asctime)s\t\t (%(name)-15.15s) (thread:%(thread)d) (line:%(lineno)5d)\t\t[%(levelname)-5.5s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # create debug file handler in working directory
        paramsViewUiPath = os.path.dirname(os.path.realpath(__file__)) + "\\lensViewUi.ui"
        os.makedirs(os.path.dirname(os.path.realpath(__file__)) + "\\log", exist_ok=True)
        handler = RotatingFileHandler(os.path.dirname(os.path.realpath(__file__)) + "\\log\\virus-propagation-simulator.log",maxBytes=2.3 * 1024 * 1024, backupCount=5)
        handler.setLevel(logging.ERROR)
        formatter = logging.Formatter(
            "%(asctime)s\t\t (%(name)-25.25s) (thread:%(thread)d) (line:%(lineno)5d)\t\t[%(levelname)-5.5s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    @staticmethod
    def handle_exception(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        log.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


def main():
    # Makes the icon in the taskbar as well.
    appID = "M-AFK"  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appID)
    app = App(sys.argv)
    app.setWindowIcon(QIcon(os.path.dirname(os.path.realpath(__file__)) + "\\gui\\misc\\logo\\logo1.png"))
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()