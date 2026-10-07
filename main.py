import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import webview
# from selenium import webdriver # in case
# import requests # in case
# from flask import Flask # in case


root = tk.Tk()
root.geometry("1600x900")
webview.create_window("Outlook Login", "html.html")
webview.start()

