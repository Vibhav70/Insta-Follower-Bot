from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

USERNAME = "{ENTER YOUR USERNAME}"
PASSWORD = "{ENTER YOUR PASSWORD}"
URL = "{ENTER URL OF THE TARGET PROFILE}"


class Reel:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def quote_searching(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)


    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(4)
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        time.sleep(4)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        not_now = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        not_now.click()
        time.sleep(5)
        # not_now2 = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        # not_now2.click()
        self.driver.get(URL)
        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)


    def follow(self):
        follower_list = self.driver.find_elements(By.CSS_SELECTOR, '._aano div button')
        for follower1 in follower_list:
            try:
                follower1.click()
                time.sleep(5)
            except ElementClickInterceptedException:
                self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/button/div/div')
                time.sleep(5)

bot = Reel()
bot.login()
time.sleep(2)
bot.find_followers()
bot.follow()
bot.quote_searching()