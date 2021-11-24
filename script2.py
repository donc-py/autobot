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

driver.get("https://www.facebook.com/messages/t/ryan.sepiol.1")
#Configurar de acuerdo al usuario de cada cuenta que se vala a fijar

print("Por favor loguearse con el qr generado en pantalla/ YES/NO?")
resp = input("Ingrese su repuesta")

if resp == "YES":
    while True:
        print("logged")
        mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1',
                                             port='3306')
        cursor1 = mariadb_connection.cursor()
        que = "SELECT * FROM bots WHERE id=2;"
        dc = pd.read_sql_query(que, mariadb_connection)

        for index, valor in dc.iterrows():
            if valor['status'] == 'off':
                driver.close()

        #'//*[@id="email"]'  '//*[@id="pass"]' '//*[@id="u_0_2"]'

        chats = driver.find_elements(By.XPATH,
                                    '/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/ul/li/div[1]/a/div')

        #chats = driver.find_elements_by_class_name('_1ht5 _2il3 _6zka _5l-3 _3itx')
        try:

            driver.find_element_by_xpath('//*[@id="js_h"]/li/a').click()
            print("new message from New user")
            time.sleep(5)
            chats = driver.find_elements(By.XPATH,
                                         '/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/ul/li/div[1]/a/div')

            idchat = 0
            print(len(chats))

            for chat in chats:
                idchat = idchat + 1

                name = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/ul/li[{}]/div[1]/a/div/div[2]/div[1]/span'.format(
                        idchat)).text
                print(name)

                try:
                    # newchat = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/ul/li[{}]/div[2]/div/div[2]'.format(idchat))
                    driver.find_element_by_class_name('_6zv_')
                    print("New message")
                    name = driver.find_element_by_xpath(
                        '/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/ul/li[{}]/div[1]/a/div/div[2]/div[1]/span'.format(
                            idchat)).click()
                    time.sleep(4)
                    # '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[4]/div/div[2]/div[2]/div' \
                    # '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[4]/div/div[2]/div[{}]/div'
                    # '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[{}]'
                    datamess = driver.find_elements_by_xpath(
                        '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div')
                    print(len(datamess))
                    idbucle = 0
                    for buclemess in datamess:
                        idbucle = idbucle + 1
                        # print(idbucle)
                        if idbucle == len(datamess):
                            datamsj = driver.find_elements_by_xpath(
                                '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[{}]/div/div[2]/div'.format(
                                    idbucle))
                            # print(len(datamsj))
                            idmsj = 0
                            for msj in datamsj:
                                idmsj = idmsj + 1
                                if idmsj == len(datamsj):
                                    lastmsj = driver.find_element_by_xpath(
                                        '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[{}]/div/div[2]/div[{}]'.format(
                                            idbucle, idmsj)).text
                                    print(lastmsj)
                                    que2 = "SELECT * FROM questions;"
                                    dc2 = pd.read_sql_query(que2, mariadb_connection)
                                    notmatch = False

                                    for index, valor in dc2.iterrows():
                                        if str(valor['question']).lower() == lastmsj.lower():
                                            notmatch = True
                                            print(valor['response'])
                                            try:

                                                driver.find_element_by_class_name('notranslate').click()
                                                print('clicked')
                                                actions = ActionChains(driver)

                                                print('pass text box')
                                                actions.send_keys(str(valor['response']))
                                                actions.perform()
                                                print('pass send text box')
                                                time.sleep(1)
                                                driver.find_element_by_xpath(
                                                    '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/a').click()
                                            except NoSuchElementException:
                                                print("not send msj")
                                    if notmatch == False:
                                        driver.find_element_by_class_name('notranslate').click()
                                        print('clicked')
                                        actions = ActionChains(driver)

                                        print('pass text box')
                                        actions.send_keys(str(
                                            "No entiendo su mensaje, por favor especifique su requerimento con mayor claridad"))
                                        actions.perform()
                                        print('pass send text box')
                                        time.sleep(1)
                                        driver.find_element_by_xpath(
                                            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[3]/a').click()


                    # '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[5]/div/div[2]/div[4]' \
                    # '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[5]/div/div[2]/div[{}]'

                    # '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[5]' \
                    # '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[{}]'

                except NoSuchElementException:
                    print("not found")

            driver.get("https://www.facebook.com/messages")
            time.sleep(8)

        except NoSuchElementException:
                print("No new messages")



        idchat = 0
        print(len(chats))

        for chat in chats:
            idchat = idchat + 1

            name = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/ul/li[{}]/div[1]/a/div/div[2]/div[1]/span'.format(idchat)).text
            print(name)

            try:
                #newchat = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/ul/li[{}]/div[2]/div/div[2]'.format(idchat))
                driver.find_element_by_class_name('_6zv_')
                print("New message")
                name = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/ul/li[{}]/div[1]/a/div/div[2]/div[1]/span'.format(
                        idchat)).click()
                time.sleep(4)
                #'/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[4]/div/div[2]/div[2]/div' \
                #'/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[4]/div/div[2]/div[{}]/div'
                #'/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[{}]'
                datamess = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div')
                print(len(datamess))
                idbucle = 0
                for buclemess in datamess:
                    idbucle = idbucle + 1
                    #print(idbucle)
                    if idbucle == len(datamess):
                        datamsj = driver.find_elements_by_xpath(
                            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[{}]/div/div[2]/div'.format(idbucle))
                        #print(len(datamsj))
                        idmsj = 0
                        for msj in datamsj:
                            idmsj = idmsj +1
                            if idmsj == len(datamsj):
                                lastmsj = driver.find_element_by_xpath(
                                    '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[{}]/div/div[2]/div[{}]'.format(
                                        idbucle,idmsj)).text
                                print(lastmsj)
                                que2 = "SELECT * FROM questions;"
                                dc2 = pd.read_sql_query(que2, mariadb_connection)
                                notmatch = False

                                for index, valor in dc2.iterrows():
                                    if str(valor['question']).lower() == lastmsj.lower():
                                        notmatch = True
                                        print(valor['response'])
                                        try:

                                            driver.find_element_by_class_name('notranslate').click()
                                            print('clicked')
                                            actions = ActionChains(driver)

                                            print('pass text box')
                                            actions.send_keys(str(valor['response']))
                                            actions.perform()
                                            print('pass send text box')
                                            time.sleep(1)
                                            driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/a').click()
                                        except NoSuchElementException:
                                            print("not send msj")
                                if notmatch == False:
                                    driver.find_element_by_class_name('notranslate').click()
                                    print('clicked')
                                    actions = ActionChains(driver)

                                    print('pass text box')
                                    actions.send_keys(str("No entiendo su mensaje, por favor especifique su requerimento con mayor claridad"))
                                    actions.perform()
                                    print('pass send text box')
                                    time.sleep(1)
                                    driver.find_element_by_xpath(
                                        '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/a').click()

                #'/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[5]/div/div[2]/div[4]' \
                #'/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[5]/div/div[2]/div[{}]'

                #'/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[5]' \
                #'/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[{}]'

            except NoSuchElementException:
                print("not found")
        driver.get("https://www.facebook.com/messages/t/ryan.sepiol.1")
        time.sleep(8)



