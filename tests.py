import win32api
import win32gui
import win32con


def click(x, y):
    hWnd = win32gui.FindWindow(None, "Minecraft* 1.16.5 - Singleplayer")
    lParam = win32api.MAKELONG(x, y)

    hWnd1= win32gui.FindWindowEx(hWnd, None, None, None)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONUP, None, lParam)

while True:
    click(100,100)