from url_pages import Login
def test_login(browser):
    login_main_page=Login(browser)
    login_main_page.go_to_site()
    login_main_page.username('standard_user')
    login_main_page.pas('secret_sauce1')
    login_main_page.click()
    login_main_page.check_login()