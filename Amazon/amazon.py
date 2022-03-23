from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class Amazon:
    http_list = list()
    info_list=list()
    check_book=list()
    #Драйвер
    def selenium_amazon(self,sait,filter_xpath,poisk,urlik):
        print('Wait...')
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.headless = True
        driver = webdriver.Chrome(
            executable_path='/Users/ostap/Desktop/OldFiles/TestMatick/chromedriver',
            options=options)
        driver.get(url=f'{sait}')
        driver.find_element_by_xpath(f'{filter_xpath}').click()
        time.sleep(1)
        poisk_in=driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
        poisk_in.clear()
        poisk_in.send_keys(f'{poisk}')
        poisk_in.send_keys(Keys.ENTER)

#------------------------
        def information_about_book(url_book):
            driver.get(url=f'{url_book}')
            name_book = driver.find_element_by_css_selector('#productTitle').text
            author_book = driver.find_element_by_xpath('//*[@id="bylineInfo"]').text
            author_book = author_book.replace('by', '')
            author_book = author_book.replace('(Author)', '')
            author_book = author_book.strip()
            try:
                price_book = driver.find_element_by_xpath(
                    '//*[@id="mediaOlp"]/div/div/div/div[1]/div[2]/span[1]/a/span[2]').text
            except NoSuchElementException:
                price_book = 'No price'
            try:
                best_sellet_book = driver.find_element_by_xpath(
                    '//*[@id="zeitgeistBadge_feature_div"]/div/a/i').text
            except NoSuchElementException:
                best_sellet_book = 'Not Best Seller'
            info_book = [name_book, author_book, price_book, best_sellet_book]
            return info_book
        for i in range(1,100):
            try:
                https=driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[{i}]/div/span/div/div/div[2]/div[2]/div/div/div[1]/h2/a').get_attribute('href')
            except NoSuchElementException:
                break
            finally:
                self.http_list.append(https)
        for i in self.http_list:
            self.info_list.append(information_about_book(i))

        if urlik!=None:
            self.check_book=information_about_book(urlik)














