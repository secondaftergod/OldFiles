from selenium import webdriver
import selenium
import time
from fake_useragent import UserAgent
from multiprocessing.pool import ThreadPool
from selenium.webdriver.common.keys import Keys

#add options to Chrome----------------------------------------:
options = webdriver.ChromeOptions()
#fake_useragent
useragent = UserAgent(verify_ssl=False)
options.add_argument(f'user-agent={useragent.random}')
#--------------------------------------------------------------

url='https://bidfax.info/'
def selenium_qa(url):
    driver = webdriver.Chrome(
                executable_path='/Users/ostap/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/main/Selenium QA/chromedriver',
                options=None)
#Walk to URL:
    driver.get(url=url)
    choose_car=driver.find_element_by_xpath('/html/body/div[1]/main/section[1]/div/div/div[2]/div/div[1]/div[1]/ul/div')
    cars=choose_car.get_attribute()
    print(cars)
    #poisk=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')
    #poisk.clear()
    #poisk.send_keys('QA')
    #poisk.send_keys(Keys.ENTER)

selenium_qa(url)