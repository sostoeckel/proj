import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import webview
from selenium import webdriver
import requests

root = tk.Tk()
root.geometry("1600x900")
webview.create_window("Roblox", "https://www.roblox.com/login")
webview.start(debug=True)
