import sys
import traceback
import tkinter as tk
import webview

root = tk.Tk()
root.geometry("1600x900")
webview.create_window("Roblox Login", "https://www.roblox.com/login")
webview.start()