from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class Test:

        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.headless = True
        driver = webdriver.Chrome(
            executable_path='/TestMatick/chromedriver',
            options=options)
        driver.get(url=f'{sait}')








