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
        ##mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1',
                 #                            port='3306')
       # cursor1 = mariadb_connection.cursor()
        #que = "SELECT * FROM bots WHERE id=3;"
        #dc = pd.read_sql_query(que, mariadb_connection)

        #for index, valor in dc.iterrows():
        #    if valor['status'] == 'off':
        #        driver.close()

        #'/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]' \
        #/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div
        #'/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{}]'
        #'/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[2]/div[1]/div/div/div/div'

        chats = driver.find_elements(By.XPATH,
                                     '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/a/div')

        # chats = driver.find_elements_by_class_name('_1ht5 _2il3 _6zka _5l-3 _3itx')

        idchat = 0
        print(len(chats))

        for chat in chats:
            idchat = idchat + 1
            name = driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{}]/a/div/div[2]/div[1]/div/div/div/div'.format(
                    idchat)).text
            print(name)
            try:
                driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[3]/div')
                print("New message")
                name = driver.find_element_by_xpath(
                    '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{}]/a/div/div[2]/div[1]/div/div/div/div'.format(
                        idchat)).click()

                #'/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]' \
                #'/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[{}]'

                #'/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div' \
                #'/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div/div/div/div/div' \
                #'/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/span' \
                #'/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div/div/div/div/div/div/div/span'

                list = driver.find_elements_by_class_name('DMBLb')
                lastmsj = driver.find_elements_by_class_name('DMBLb')[len(list) - 1].text

                print(lastmsj)
                que2 = "SELECT * FROM questions;"
                dc2 = pd.read_sql_query(que2, mariadb_connection)
                notmatch = False

                for index, valor in dc2.iterrows():
                    if str(valor['question']).lower() == lastmsj.lower():
                        print(valor['response'])

                        txt_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        txt_box.send_keys(str(valor['response']))

                        driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                        driver.get("https://www.instagram.com/direct/inbox/")
                        notmatch = True


                if notmatch == False:
                    txt_box = driver.find_element_by_xpath(
                            '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    txt_box.send_keys(str("No entiendo su mensaje, por favor especifique su requerimento con mayor claridad"))

                    driver.find_element_by_xpath(
                            '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()


                    driver.get("https://www.instagram.com/direct/inbox/")


            except NoSuchElementException:
                print("not found")
        time.sleep(1)