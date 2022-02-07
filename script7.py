import undetected_chromedriver.v2 as uc
import time
driver = uc.Chrome()
driver.get('https://coinsniper.net/')  # known url using cloudflare's "under attack mode"

time.sleep(6)

driver.close()


