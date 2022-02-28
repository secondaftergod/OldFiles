from selenium_unian.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class newsPage(BasePage):
    hrefs = (By.XPATH,'//*[@id="page_content"]/div[2]/div[2]/div[1]//div/a')
    tit=(By.XPATH,'//*[@id="block_left_column_content"]/div[1]/div/h1')
    def __init__(self, driver):
        super().__init__(driver)
    def get_tite(self):
        return self.get_element_text(self.tit)

    def get_all_links(self):
        return self.get_all_elements_links(self.hrefs)



