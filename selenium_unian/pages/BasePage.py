from selenium.webdriver import ActionChains
from selenium import webdriver
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, InvalidSelectorException as EX
from selenium_unian.configuration.config import TestData as Data

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by_locator):
        try:
            WebDriverWait(self.driver, Data.EXPLICIT_WAIT).until(EC.visibility_of_element_located(by_locator)).click()

        except EX as e:
            print("Exception! Can't click on the element")

    def input_element(self, by_locator, text):
        try:
            WebDriverWait(self.driver, Data.EXPLICIT_WAIT).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except EX as e:
            print("Exception! Can't click on the element")

    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, Data.EXPLICIT_WAIT).until(EC.visibility_of_element_located(by_locator)).text


    def get_title(self):
        return self.driver.title

    def get_element_attribute(self, by_locator, attribute_name):
        element = WebDriverWait(self.driver, Data.EXPLICIT_WAIT).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute_name)

    def verify_element_displayed(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False

    def find(self, by_locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(by_locator),
                                                      message=f"Can't find element by locator {by_locator}")

    def findAll(self, by_locator, time=3):
        elements=WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(by_locator),
                                                      message=f"Can't find elements by locator {by_locator}")
        return elements
    def findAllLinks(self,by_locator,time=3):
        elements = WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(by_locator),
                                                          message=f"Can't find elements by locator {by_locator}").get_attribute("href")
        return elements
    def click_all_element(self,by_locator):
        for i in self.findAll(by_locator):
            i.click()

    def get_all_elements_text(self,by_locator):
        list_text=[]
        for i in self.findAll(by_locator):
            list_text.append(i.text)
        return list_text
    def get_all_elements_links(self,by_locator):
        list_link=[]
        for i in self.findAllLinks(by_locator):
            list_link.append(i)
        return list_link


