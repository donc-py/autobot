from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
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
import sys
import mysql.connector as mariadb

# driver = webdriver.Chrome(executable_path='/home/pc2/Downloads/geckodriver-v0.26.0-linux64/chromedriver')
#driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")

#driver.get("https://www.instagram.com/direct/inbox/")

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/")


hashtag = sys.argv[1]
user = sys.argv[2]
clave = sys.argv[3]
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(user)

driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(clave)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()

time.sleep(7)
driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()

driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(hashtag)
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button").click()
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/article/div/div/div/div[1]/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[6]/div[3]/button").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button").click()