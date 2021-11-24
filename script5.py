from selenium import webdriver
import time
import datetime
from time import gmtime, strftime
from datetime import timedelta
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pandas as pd
import json

import mysql.connector as mariadb

# driver = webdriver.Chrome(executable_path='/home/pc2/Downloads/geckodriver-v0.26.0-linux64/chromedriver')
#driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")

#driver.get("https://www.instagram.com/direct/inbox/")

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/inbox/")

print("Por favor loguearse con el qr generado en pantalla/ YES/NO?")
resp = input("Ingrese su repuesta")

if resp == "YES":
    while True:
        print("logged")