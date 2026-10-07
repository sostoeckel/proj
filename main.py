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



# for opening the new email as a new window, maybe try creating a function to open it in here then somehow call it in the html?
# ik u can do it in javascript but idk bout python
#i'll leave the bullshit here
def open_window2():
    webview.create_window("New Email", "em.html") #how do we call this in the html???
    # if button click then open new window = em.html :) i dont know