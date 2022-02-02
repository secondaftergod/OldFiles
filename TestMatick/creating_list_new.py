from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

from bs4 import BeautifulSoup
from books_new import Books
def selenium_amazon():
    print('Wait...')
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.headless = True
    driver = webdriver.Chrome(
        executable_path='/Users/ostap/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/main/TestMatick/chromedriver',
        options=options)
    html='https://www.amazon.com/s?k=python&i=stripbooks-intl-ship&crid=364PB30OJWX39&sprefix=python%2Cstripbooks-intl-ship%2C176&ref=nb_sb_noss_1'
    driver.get(url=html)
    source_data=driver.page_source
    soup = BeautifulSoup(source_data, 'html.parser')
    #books = soup.find_all('span', {'class': ['a-size-medium']})











selenium_amazon()

