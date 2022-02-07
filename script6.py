from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import sys
import time
from selenium.common.exceptions import NoSuchElementException

hashtag_list = ['antiques', 'antiquesroma', 'antiquesautions']

prev_user_list = []
#- if it's the first time you run it, use this line and comment the two below
#prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2]  # useful to build a user log
#prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0
webdriver = webdriver.Firefox()
webdriver.get("https://www.instagram.com/")


hashtag = sys.argv[1]
user = sys.argv[2]
clave = sys.argv[3]
time.sleep(3)
webdriver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(user)

webdriver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(clave)
webdriver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()

time.sleep(9)

try:
    webdriver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
    time.sleep(3)
    webdriver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
#        url = driver.find_element_by_xpath(
#            "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{}]/a[1]/div[1]/img".format(
#                count))
#        src = url.get_attribute('src')
#        count = count + 1
 #       print(src)
except NoSuchElementException:
    print("not found")
    webdriver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]").click()
    #    driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()


for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
    sleep(5)
    first_thumbnail = webdriver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

    first_thumbnail.click()
    sleep(randint(3, 4))
    try:
        for x in range(1, 200):
            "/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a"

            username = webdriver.find_element_by_xpath(
                "/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a").text

            if username:
                print(username)

                # If we already follow, do not unfollow
                try:
                    "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button"
                    "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]"

                    if webdriver.find_element_by_css_selector("button.sqdOP:nth-child(2)").text == "Follow":
                        webdriver.find_element_by_css_selector("button.sqdOP:nth-child(2)").click()
                        new_followed.append(username)
                        followed += 1
                    #print(webdriver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button").text)
                    else:
                    #webdriver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button").click()
                        print('followed')

                except NoSuchElementException:
                    print("not found followed")

                try:
                    # Liking the picture
                    ".fr66n > button:nth-child(1)"

                    button_like = webdriver.find_element_by_css_selector(".fr66n > button:nth-child(1)")

                    button_like.click()
                    likes += 1
                    sleep(randint(18, 25))
                except NoSuchElementException:
                    print("not found liked")

                    # Comments and tracker
                comm_prob = randint(1, 10)
                print('{}_{}: {}'.format(hashtag, x, comm_prob))
                if comm_prob > 7:
                    comments += 1
                    webdriver.find_element_by_xpath(
                        '/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[2]/button/span').click()
                    comment_box = webdriver.find_element_by_xpath(
                        '/html/body/div[3]/div/div[2]/div/article/div[2]/section[3]/div/form/textarea')


                    # Enter to post comment
                    comment_box.send_keys(Keys.ENTER)
                    sleep(randint(5, 7))

                # Next picture
                webdriver.find_element_by_css_selector(".l8mY4 > button:nth-child(1)").click()
                #webdriver.find_element_by_link_text('Next').click()
                sleep(randint(5, 7))
            else:
                webdriver.find_element_by_css_selector(".l8mY4 > button:nth-child(1)").click()
                sleep(randint(5, 7))
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue

for n in range(0, len(new_followed)):
    prev_user_list.append(new_followed[n])

updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv("cs{}users_followed_list.csv".format(strftime('%Y%m%d')))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))