from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import random
import subprocess
numbers_red=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
win_number_list=[]
#-------------------Money information-------------------------------------
def money_info(balance):
    with open('money_ostap.txt', 'w') as file_out:
        file_out.write(f'На рахунку {str(balance)} гривень')
print('Choose your Win:')
limit_to_win=float(input())
# -------------------------------------------------------------

# add options to Chrome----------------------------------------:
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')

# --------------------------------------------------------------

def selenium_parimatch():
    driver = webdriver.Chrome(
        executable_path='/Users/ostap/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/main/Selenium PARIMATCH/chromedriver',
        options=options)

    # -----------------------LOGIN-------------------------
    driver.get(url='https://parimatch.com/ru/login')
    time.sleep(8)

    def login():
        login = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/form/div[1]/div[1]/div[2]/div[2]/input')
        login.click()
        login.send_keys('674796070')
        time.sleep(1.5)

        password = driver.find_element_by_xpath('//*[@id="password"]')
        password.click()
        password.send_keys('0ybtkpo8Element')
        time.sleep(1.5)

        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/form/button/span').click()
        time.sleep(2)

        if driver.current_url == 'https://parimatch.com/ru/login':
            time.sleep(15)
            login = driver.find_element_by_xpath(
                '//*[@id="root"]/div[2]/div[2]/div/form/div[1]/div[1]/div[2]/div[2]/input')
            login.click()
            login.send_keys('674796070')
            time.sleep(1.5)

            password = driver.find_element_by_xpath('//*[@id="password"]')
            password.click()
            password.send_keys('0ybtkpo8Element')
            time.sleep(1.5)

            driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/form/button/span').click()
            time.sleep(3)
        else:
            time.sleep(3)

    login()

    # -------------------------------------Walk to GAME-----------------------------:
    def to_game():
        driver.get(url='https://parimatch.com/ru/casino/live-casino/game/eva-lc-pragmatic-speedroulette-203')
        print('Wait to loading page...')
        time.sleep(1)
        driver.refresh()
        time.sleep(10)
        driver.get(driver.current_url)
        time.sleep(7)
        print('Loading DONE')

    to_game()

    # ------------------------GET BALANCE--------------------
    def get_balance():
        time.sleep(0.2)
        balance = driver.find_element_by_css_selector('#footer-main > div.footer_left > div.bal_div > label').text
        balance_float = re.sub(r'₴', '', balance)
        balance_float1 = re.sub(r',', '.', balance_float)
        balance_float2 = re.sub(r' ', '', balance_float1)
        balance_total = float(balance_float2)
        return balance_total

    #------------------Statistic--------------
    def statistic():
        time.sleep(0.2)
        total=driver.find_element_by_css_selector('#footer-main > div.footer_right > div > div > label').text
        balance_push = re.sub(r'₴', '', total)
        balance_push1 = re.sub(r',', '.', balance_push)
        balance_push2 = re.sub(r' ', '', balance_push1)
        total_stat = float(balance_push2)
        return total_stat

    def total_push(push):
        with open('money_in_now_ostap.txt', 'w') as file_out:
            file_out.write(f'Ставка {str(push)} гривень')

    def total_statistic(stat):
        with open('statistic_ostap.txt', 'a') as file_out:
            file_out.write(f'{str(stat)}\n')

    # ---------------Choose_chips----------
    def double_chips():
        double = driver.find_element_by_xpath('//*[@id="double-btn"]')
        time.sleep(0.25)
        double.click()

    #----------------Numbers_information-------------
    def about_win():
        last_number = driver.find_element_by_css_selector(
            '#ministats-container > div > app-single-row-stats > div > table > tbody > tr > td:nth-child(1)')
        if int(last_number.text) in numbers_red:
            win_number_list.append('red')
        else:
            win_number_list.append('black')
    def choose_color_if_4():
        try:
            if win_number_list.count(win_number_list[0])==4:
                return win_number_list[0]
        except IndexError:
            pass
        if len(win_number_list)==4:
            win_number_list.pop(0)
            return 'wait'
        return 'wait'
    # ---------------Start_game_red----------
    def game_start_red():
        try:
            WebDriverWait(driver, 300, poll_frequency=0.1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.svgBetBoard.active')))
        finally:
            red = driver.find_element_by_css_selector('#dz48') #RED
            #red = driver.find_element_by_css_selector('#dz46')  #/2=0
            time.sleep(0.25)
            red.click()
            time.sleep(0.15)
            double_chips()
            #time.sleep(0.15)
            #double_chips()


            
    # ---------------Start_game_black----------
    def game_start_black():
        try:
            WebDriverWait(driver, 300, poll_frequency=0.1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.svgBetBoard.active')))
        finally:
            black = driver.find_element_by_css_selector('#dz49') #BLACK
            #black = driver.find_element_by_css_selector('#dz51')
            time.sleep(0.25)
            black.click()
            time.sleep(0.15)
            double_chips()
            #time.sleep(0.15)

    # ---------------Random_color----------
    def random_colors():
        random_color = random.randint(0, 1)
        color=choose_color_if_4()
        #if color=='red':
            #win_number_list.pop(0)
            #game_start_black()
        #elif color=='black':
           # win_number_list.pop(0)
            #game_start_red()
        if random_color == 0:
            game_start_black()
        else:
            game_start_red()

    # -------------Game_Instruction--------------
    def game_start():
        try:
            WebDriverWait(driver, 300, poll_frequency=0.1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.svgBetBoard.active')))
        finally:
            time.sleep(2.0)
            about_win()
            random_colors()
            time.sleep(0.1)
            total_push(statistic())
        time.sleep(13.7)


    def game_next(balance,start_money):
        step=0
        try:
            WebDriverWait(driver, 300, poll_frequency=0.1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.svgBetBoard.active')))
        finally:
            time.sleep(2.0)
            new_balance = get_balance()
        if balance<=new_balance:
            total_statistic(4.0)#тут розмір ставки для статистики
        elif new_balance>=start_money+limit_to_win:#choose limit to win
            time.sleep(4)
            driver.close()
        while balance > new_balance:
            about_win()
            step += 1
            if step==10:#save half
                time.sleep(5)
                driver.close()
            random_colors()
            for i in range(step):
                double_chips()
                time.sleep(0.3)
            stat1=statistic()
            total_push(stat1)
            time.sleep(13.7)
            try:
                WebDriverWait(driver, 300, poll_frequency=0.1).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.svgBetBoard.active')))
            finally:
                time.sleep(2)
                if new_balance==get_balance():
                    step-=1
                else:
                    new_balance = get_balance()
                if balance < new_balance:
                    total_statistic(stat1)#тут розмір ставки для статистики
                elif new_balance >= start_money + limit_to_win:  # choose limit to win
                    time.sleep(4)
                    driver.close()


    #---------------Game-----------------
    start_balance=get_balance()
    while True:
        balance = get_balance()
        money_info(balance)
        game_start()
        game_next(balance,start_balance)

selenium_parimatch()
