from selenium.webdriver.common.by import By

from pageObjects.shopPage import ShopPage
from utils.browserutils import Browser_utils


class LoginPage(Browser_utils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.loginBtn = (By.ID, 'signInBtn')

    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.loginBtn).click()
        shop_page = ShopPage(self.driver)
        return shop_page