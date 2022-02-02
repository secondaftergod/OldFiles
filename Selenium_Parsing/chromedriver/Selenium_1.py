from selenium import webdriver
import time
from fake_useragent import UserAgent
from multiprocessing.pool import ThreadPool
from podmena import multi_list
from selenium.webdriver.common.keys import Keys


#multi opening class POOL
url_multi=list()
for i in range(10):
    url_multi.append(multi_list())
#add options to Chrome----------------------------------------:
options = webdriver.ChromeOptions()

#fake_useragent
useragent = UserAgent(verify_ssl=False)
options.add_argument(f'user-agent={useragent.random}')

#PROXY
"""PROXY = "138.128.91.65:8000"
options.add_argument('--proxy-server=%s' % PROXY)"""

#whitout opening Chrome using all clicks and wrote
options.headless = True

#disable webdriver for rogue
options.add_argument('--disable-blink-features=AutomationControlled')
#--------------------------------------------------------------

#Chromedriver connection

def multi_potok(url):
    try:
        driver = webdriver.Chrome(
            executable_path='/Users/ostap/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/main/Selenium_Parsing/chromedriver/chromedriver',
            options=options)
        #Walk to URL
        driver.get(url=url)
        time.sleep(3)
        #Searching elements
        #spam=driver.find_element_by_id('inputmsg')
        spam=driver.find_element_by_xpath('//*[@id="inputmsg"]')
        time.sleep(1)
        #Clear
        spam.clear()
        #Write wthat you want
        print('SEND')
        spam.send_keys('Слишком много багов на вашем сайте,что бы оплатить Ваш курс')
        time.sleep(1.5)
        spam.send_keys(Keys.ENTER)
        time.sleep(1)

        out=driver.find_element_by_xpath('/html/body/section/div[1]/div[2]/a').click()
        time.sleep(1.5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    for i in range(5):
        ThreadPool(10).map(multi_potok,url_multi)

