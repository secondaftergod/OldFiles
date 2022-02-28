from configuration.config import Browser,TestData
from pages.newsPage import newsPage

def launch():
    if TestData.BROWSER=='chrome':
        driver = Browser()
        driver.get(TestData.URL)
        news=newsPage(driver)
        print(news.get_tite())
        print(news.get_all_links())
    else:
        raise ValueError('Browser is not supported')

launch()