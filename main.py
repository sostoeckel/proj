import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import webview
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests

root = tk.Tk()
root.geometry("1600x900")
webview.create_window("Roblox Login", "https://www.roblox.com/login")
webview.start()
'''
# test 1 to use login button to get info to load home page
driver = webdriver.Chrome()
driver.get("https://www.roblox.com/login")
button = driver.find_element_by_id('login-button')
button.click()
if button.click():
    webview.create_window("Roblox Login", "https://www.roblox.com/home")
    webview.start()

# test 2 of previous
with requests.Session() as s:
    s.get('https://www.roblox.com/login')
    final_page = s.get('https://www.roblox.com/home')
    print(final_page.text)
'''
import requests
from bs4 import BeautifulSoup

LOGIN_URL = "https://quotes.toscrape.com/login"
USERNAME = "your-username"
PASSWORD = "your-password"

session = requests.Session()

# GET the form first to receive a fresh CSRF token and cookies.
login_page = session.get(LOGIN_URL)
soup = BeautifulSoup(login_page.text, "html.parser")
token = soup.find("input", {"name": "csrf_token"})["value"]

payload = {
    "csrf_token": token,
    "username": USERNAME,
    "password": PASSWORD,
}

response = session.post(LOGIN_URL, data=payload)
response.raise_for_status()

# The site shows a "Logout" link only when authenticated.
if "Logout" in response.text:
    print("Login succeeded; session cookies:", session.cookies.get_dict())
else:
    print("Login failed; still on the sign-in page.")