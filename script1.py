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
driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")

driver.get("https://web.whatsapp.com/")

print("Por favor loguearse con el qr generado en pantalla/ YES/NO?")
resp = input("Ingrese su repuesta")

if resp == "YES":
    while True:
        print("logged")
        mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1',
                                             port='3306')
        cursor1 = mariadb_connection.cursor()
        que = "SELECT * FROM bots WHERE id=1;"
        dc = pd.read_sql_query(que, mariadb_connection)

        for index, valor in dc.iterrows():
            if valor['status'] == 'off':
                driver.close()

        chats3 = driver.find_elements_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div')
        chats = driver.find_elements(By.XPATH,
                                     '//*[@id="pane-side"]/div[1]/div/div/div')
        chats2 = driver.find_elements(By.XPATH,
                                      '//*[@id="pane-side"]/div[1]/div/div/div/div/div/div[2]')

        idchat = 0
        print(len(chats))

        for chat in chats:

            idchat = idchat + 1
            name = driver.find_element_by_xpath(
                '//*[@id="pane-side"]/div[1]/div/div/div[{}]/div/div/div/div[2]/div[1]/div[1]/span/span'.format(
                    idchat)).text

            try:
                messa = driver.find_element_by_xpath(
                    '//*[@id="pane-side"]/div[1]/div/div/div[{}]/div/div/div/div[2]/div[2]/div[2]/span[1]/div/span'.format(
                        idchat)).text
                driver.find_element(By.XPATH,
                                    '//*[@id="pane-side"]/div[1]/div/div/div[{}]/div/div/div/div[2]/div[1]/div[1]/span/span'.format(
                                        idchat)).click()
                time.sleep(2)
                allm = driver.find_elements_by_class_name('message-in')

                mess = driver.find_elements_by_class_name('message-in')[len(allm) - 1].text

                print(mess)
                que2 = "SELECT * FROM questions;"
                dc2 = pd.read_sql_query(que2, mariadb_connection)

                notmatch = False

                for index, valor in dc2.iterrows():
                    if str(valor['question']).lower() == mess.lower():
                        notmatch = True
                        txt_box = driver.find_element_by_xpath(
                            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                        txt_box.send_keys(str(valor['response']))
                        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
                if notmatch == False:
                    txt_box = driver.find_element_by_xpath(
                        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    txt_box.send_keys(str("No entiendo su mensaje, por favor especifique su requerimento con mayor claridad"))
                    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()



            except NoSuchElementException:
                print("No new messages")



