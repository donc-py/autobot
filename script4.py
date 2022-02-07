import time
from time import gmtime, strftime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import mysql.connector as mariadb
import sys
from bs4 import BeautifulSoup
import requests
import json

headers = {  # <-- so the Google will treat your script as a "real" user browser.
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

#response = requests.get(
#  'https://www.google.com/search?q={}&tbm=shop'.format(sys.argv[1]),
#  headers=headers).text

#soup = BeautifulSoup(response, 'html.parser')

#data = []

#print(soup)

#for container in soup.findAll('div', class_='sh-dgr__content'):
  #title = container.find('h4', class_='A2sOrd').text
  #price = container.find('span', class_='a8Pemb').text
  #supplier = container.find('div', class_='aULzUe IuHnof').text

  # data.append({
  #  "Title": title,
  #  "Price": price,
  #  "Supplier": supplier,
  #})

#print(json.dumps(data, indent = 2, ensure_ascii = False))
driver = webdriver.Firefox()
driver.get("https://www.google.com/")
import csv
import bs4
import requests
import re
def is_price(tag):
    for k, v in tag.attrs.items():
        if 'price' in v:
            return True
        elif isinstance(v, list) and any('price' in i for i in v):
            return True

header = ['Cod', 'Product', 'E-shop Link Found', 'prices related']

print(sys.argv[1])

key = sys.argv[1].replace("-", " ")

print(key)
#mariadb_connection = mariadb.connect(user='agarjoya_testscrap', password='Y}0Kc+XrawU.',database='agarjoya_testscrap', host='127.0.0.1', port='3306')
#cursor = mariadb_connection.cursor()


driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(key)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
"/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[1]/a/div/cite"
"/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[4]/div/div/div[1]/a/div/cite"
"/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[5]/div/div/div[1]/a/div/cite"
"/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[6]/div/div/div[1]/a/div/cite"
"/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[7]/div/div/div[1]/a/div/cite"
"/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[10]/div/div/div[1]/a/div/cite"

driver.find_element_by_xpath("/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a").click()
SCROLL_PAUSE_TIME = 1.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
time.sleep(3)
elem = driver.find_elements_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div/a[1]/div[1]/img")

"/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img"
"/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[2]/a[1]/div[1]/img"
print(len(elem))

lnks=driver.find_elements_by_tag_name("a")



with open('search_{}_{}.csv'.format(sys.argv[1],strftime("%H_%M_%S", gmtime())), 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    # traverse list
    count = 0
    for lnk in lnks:
        # get_attribute() to get all href
        print(lnk.get_attribute('href'))
        if lnk.get_attribute('href') != None:
            if "google" in lnk.get_attribute('href'):
                print("Found")
            else:
                print("Not Found")
                u = lnk.get_attribute('href')
                try:
                    r = requests.get(u)
                    c = r.content
                    soup = bs4.BeautifulSoup(c, "html.parser")
                    print(len(soup.find_all(is_price)))

                    countag = 0

                    for tag in soup.find_all(is_price):

                        if countag == 0:
                            print(tag)
                            y = str(tag)
                            x = re.findall("[0-9]+", y)
                            print(x)
                            act = False
                            for i in x:
                                i = int(i)
                                if i <= 200:
                                    data = [count, sys.argv[1], lnk.get_attribute('href'), x]
                                    writer.writerow(data)
                                    break

                        countag = countag + 1

                    #data = [count, sys.argv[1], lnk.get_attribute('href')]
                    #writer.writerow(data)
                except:
                    print("Net Issue")
            count = count + 1



#count = 3
#for elem in elem:
#    try:
#        url = driver.find_element_by_xpath(
#            "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{}]/a[1]/div[1]/img".format(
#                count))
#        src = url.get_attribute('src')
#        count = count + 1
 #       print(src)
#    except NoSuchElementException:
 #       print("not found")
    #    driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()

##driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/input").send_keys("testname34")

#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input").send_keys("testnameput")
#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys("testnameQQQ")


#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("testnameQQQ")

#try:
#    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div")
 #   print("User Not Available")
#except NoSuchElementException:
 #   print("not found")
#    driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
