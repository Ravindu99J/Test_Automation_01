from selenium.webdriver.common.by import By

from pageObjects.checkout_confirmation import Checkout_Confirmation
from utils.browserutils import Browser_utils


class ShopPage(Browser_utils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, 'a[href*="shop"]')
        self.products_cards = (By.XPATH, "//div[@class='card h-100']")
        self.cart_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_product_to_cart(self, product_name):
        self.driver.find_element(*self.shop_link).click()

        products = self.driver.find_elements(*self.products_cards)
        for product in products:
            if product.find_element(By.XPATH, 'div/h4/a').text == product_name:
                product.find_element(By.XPATH, 'div/button').click()

    def goto_cart(self):
        self.driver.find_element(*self.cart_button).click()
        checkout_confirmation = Checkout_Confirmation(self.driver)
        return checkout_confirmation
