from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL_INSTA = "ACCOUNT EMAIL"
PASSWORD_INSTA = "ACCOUNT PASSWORD"
PAGE_INSTA = "INSTAGRAM PAGE"


class InstaFollower:
    def __init__(self):
        self.driver_patch = webdriver.ChromeOptions()
        self.driver_patch.add_experimental_option("detach", True)
        self.driver_patch.add_argument("start-maximized")
        self.driver = webdriver.Chrome(self.driver_patch)

    def login(self,user,password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        self.driver.find_element(By.XPATH, value="/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]").click()
        self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(user)
        self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(password, Keys.ENTER)
        time.sleep(3)
        try:
            self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div").click()
        finally:
            pass
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
        finally:
            pass

    def find_followers(self, insta_page):
        self.driver.get(insta_page)
        time.sleep(1)
        self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

    def follow(self):
        pop_up = self.driver.find_element(By.XPATH,
                                          value="/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        scroll_script = "arguments[0].scrollTop = arguments[0].scrollHeight;"
        self.driver.execute_script(scroll_script, pop_up)
        list_followers = self.driver.find_elements(By.CSS_SELECTOR, value="div button")
        for follow in list_followers[2:]:
            if follow.text == "Follow":
                try:
                    follow.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    self.driver.find_element(By.XPATH, value="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]").click()
        time.sleep(2)


bot = InstaFollower()
bot.login(EMAIL_INSTA,PASSWORD_INSTA)
bot.find_followers(PAGE_INSTA)
start_time = time.time()
while (time.time() - start_time) < 3000:
    bot.follow()