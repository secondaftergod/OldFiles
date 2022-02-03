from base_page import BasePage
from selenium.webdriver.common.by import By

class URLSeacrhLocators:
    LOCATOR_URL_SEARCH_User_name = (By.ID, "user-name")
    LOCATOR_URL_SEARCH_passowrd = (By.ID, "password")
    LOCATOR_URL_NAVIGATION_Login = (By.ID, "login-button")
    LOCATOR_URL_NAVIGATION_Error_login=(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
    LOCATOR_URL_NAVIGATION_Login_successful=(By.XPATH,'//*[@id="shopping_cart_container"]/a')

class Login(BasePage):

    def username(self,login):
        user_name=self.find_element(URLSeacrhLocators.LOCATOR_URL_SEARCH_User_name)
        user_name.send_keys(login)
        return user_name
    def pas(self,password):
        user_passwod=self.find_element(URLSeacrhLocators.LOCATOR_URL_SEARCH_passowrd)
        user_passwod.send_keys(password)
        return user_passwod
    def click(self):
        return self.find_element(URLSeacrhLocators.LOCATOR_URL_NAVIGATION_Login).click()

    def login_successful(self):
        return self.find_element(URLSeacrhLocators.LOCATOR_URL_NAVIGATION_Login_successful)

    def check_login(self):
        return self.check_error(URLSeacrhLocators.LOCATOR_URL_NAVIGATION_Error_login)


