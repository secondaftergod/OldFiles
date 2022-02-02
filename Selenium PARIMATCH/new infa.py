from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import random
import subprocess
# add options to Chrome----------------------------------------:
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36')

# --------------------------------------------------------------

def selenium_parimatch():
    driver = webdriver.Chrome(
        executable_path='/Users/ostap/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/main/Selenium PARIMATCH/chromedriver',
        options=options)

    # -----------------------LOGIN-------------------------
    driver.get(url='https://parimatch.com/ru/login')
    time.sleep(8)

    def login():
        login = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/form/div[1]/div[1]/div[2]/div[2]/input')
        login.click()
        login.send_keys('662535458')
        time.sleep(1.5)

        password = driver.find_element_by_xpath('//*[@id="password"]')
        password.click()
        password.send_keys('0ybtkpo8Alesia')
        time.sleep(1.5)

        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/form/button/span').click()
        time.sleep(2)

        if driver.current_url == 'https://parimatch.com/ru/login':
            time.sleep(15)
            login = driver.find_element_by_xpath(
                '//*[@id="root"]/div[2]/div[2]/div/form/div[1]/div[1]/div[2]/div[2]/input')
            login.click()
            login.send_keys('662535458')
            time.sleep(1.5)
            password = driver.find_element_by_xpath('//*[@id="password"]')
            password.click()
            password.send_keys('0ybtkpo8Alesia')
            time.sleep(1.5)

            driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/form/button/span').click()
            time.sleep(3)
        else:
            time.sleep(3)

    login()
    def to_game():
        driver.get(url='https://parimatch.com/ru/casino/live-casino/game/eva-lc-pragmatic-speedroulette-203')
        print('Wait to loading page...')
        time.sleep(1)
        driver.refresh()
        time.sleep(10)
        driver.get(driver.current_url)
        time.sleep(7)
        print('Loading DONE')

    to_game()

    def stat_500():
        time.sleep(0.1)
        driver.find_element_by_css_selector('#stats-btn').click()
        time.sleep(0.1)
        driver.find_element_by_css_selector('#lastcalled').click()

    stat_500()

selenium_parimatch()