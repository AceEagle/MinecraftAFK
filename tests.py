import win32api
import win32gui
import win32con
import time
from pywinauto import Desktop

def click(x, y):
    windowslist = []
    windows = Desktop(backend="uia").windows()
    for w in windows:
        windowslist.append(w.window_text())
    windowtitle = str([s for s in windowslist if "Minecraft*" in s][0])
    print(windowtitle)

    hWnd = win32gui.FindWindow(None, windowtitle)
    print(hWnd)
    lParam = win32api.MAKELONG(x, y)

    #hWnd1= win32gui.FindWindowEx(hWnd, None, None, None)
    #print(hWnd1)
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)

while True:
    click(50,50)
    time.sleep(1)
    click(50, 50)
    time.sleep(1)
    click(50, 50)
    time.sleep(20)