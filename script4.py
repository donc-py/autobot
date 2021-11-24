from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import mysql.connector as mariadb
import sys
driver = webdriver.Firefox()
driver.get("https://www.google.com/")
print(sys.argv[1])
#mariadb_connection = mariadb.connect(user='agarjoya_testscrap', password='Y}0Kc+XrawU.',database='agarjoya_testscrap', host='127.0.0.1', port='3306')
#cursor = mariadb_connection.cursor()


driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(sys.argv[1])
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
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
