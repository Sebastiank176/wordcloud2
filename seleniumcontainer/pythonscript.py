url = "https://www.linkedin.com/login"

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.options import Options  
from random import randint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10)

driver.get(url)

actions = webdriver.ActionChains(driver)

time.sleep(randint(10, 30)/10)

element = driver.find_element_by_id("username")
element.click()
element.send_keys('s');
time.sleep(randint(3, 10)/10)
element.send_keys('e');
time.sleep(randint(3, 10)/10)
element.send_keys('b');
time.sleep(randint(3, 10)/10)
element.send_keys('a');
time.sleep(randint(3, 10)/10)
element.send_keys('s');
time.sleep(randint(3, 10)/10)
element.send_keys('t');
time.sleep(randint(3, 10)/10)
element.send_keys('i');
time.sleep(randint(3, 10)/10)
element.send_keys('a');
time.sleep(randint(3, 10)/10)
element.send_keys('n');
time.sleep(randint(3, 10)/10)
element.send_keys('k');
time.sleep(randint(3, 10)/10)
element.send_keys('1');
time.sleep(randint(3, 10)/10)
element.send_keys('7');
time.sleep(randint(3, 10)/10)
element.send_keys('6');
time.sleep(randint(3, 10)/10)
element.send_keys('@');
time.sleep(randint(3, 10)/10)
element.send_keys('g');
time.sleep(randint(3, 10)/10)
element.send_keys('m');
time.sleep(randint(3, 10)/10)
element.send_keys('a');
time.sleep(randint(3, 10)/10)
element.send_keys('i');
time.sleep(randint(3, 10)/10)
element.send_keys('l');
time.sleep(randint(3, 10)/10)
element.send_keys('.');
time.sleep(randint(3, 10)/10)
element.send_keys('c');
time.sleep(randint(3, 10)/10)
element.send_keys('o');
time.sleep(randint(3, 10)/10)
element.send_keys('m');

time.sleep(randint(5, 20)/10)

element = driver.find_element_by_id("password")
element.click()

element.send_keys('k');
time.sleep(randint(3, 10)/10)
element.send_keys('e');
time.sleep(randint(3, 10)/10)
element.send_keys('l');
time.sleep(randint(3, 10)/10)
element.send_keys('l');
time.sleep(randint(3, 10)/10)
element.send_keys('e');
time.sleep(randint(3, 10)/10)
element.send_keys('r');
time.sleep(randint(3, 10)/10)

element.submit()

time.sleep(randint(40, 60)/10)

url = "https://www.linkedin.com/company/bechtle"
driver.get(url)

time.sleep(randint(5, 50)/10)


element = driver.find_element_by_xpath("/html/body/div[5]/div[5]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/artdeco-dropdown/artdeco-dropdown-trigger")

element.click()
time.sleep(randint(40, 60)/10)

element = driver.find_element_by_xpath("/html/body/div[5]/div[5]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/artdeco-dropdown/artdeco-dropdown-content/div/ul/li[2]/artdeco-dropdown-item/button/span")

element.click()

height_old = 0
while True:
    # Scroll down to bottom
    height_new = randint(100, 300) + height_old
    driver.execute_script("window.scrollTo(0, {});".format(height_new))

    # Wait to load page
    time.sleep(randint(5, 30)/10)

    # Calculate new scroll height and compare with last scroll height
    max_height = driver.execute_script("return document.body.scrollHeight")
    if max_height == height_new:
        break
    elif height_new >18000:
        break     
        
    height_old = height_new
    
htmltext = driver.page_source
soup = BeautifulSoup(htmltext, "html")

driver.close()

soup2 = BeautifulSoup(htmltext, "lxml")
feed = soup2.find_all ("div", id="organization-feed")

for feed_element in soup2.find_all ("div", class_="feed-shared-text relative feed-shared-update-v2__commentary ember-view"):
#    print(feed_element)
    print(feed_element.getText())