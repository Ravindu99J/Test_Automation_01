from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class Checkout_Confirmation:

    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.CSS_SELECTOR, "input[id='country']")
        self.country_locator = (By.XPATH, "//a[text()='Srilanka']")
        self.checkbox = (By.CLASS_NAME, "checkbox.checkbox-primary")
        self.submit_button = (By.CSS_SELECTOR, "input[type='submit']")
        self.success_message = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")


    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()


    def enter_delivery_address(self, country_name):
        self.driver.find_element(*self.country_input).send_keys(country_name)
        WebDriverWait(self.driver, 10).until(visibility_of_element_located(self.country_locator))
        self.driver.find_element(*self.country_locator).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()


    def validate_order(self):
        message = self.driver.find_element(*self.success_message).text
        assert "Success" in message
