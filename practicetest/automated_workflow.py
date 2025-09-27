
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

chrom_opt = webdriver.ChromeOptions()
chrom_opt.add_argument('--headless')
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element(By.CSS_SELECTOR,'a[href*="shop"]').click()
# driver.find_element(By.CSS_SELECTOR,"app-card-list app-card:first-child button[class='btn btn-info']").click()

products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    if product.find_element(By.XPATH,'div/h4/a').text == 'Blackberry' :
        product.find_element(By.XPATH,'div/button').click()


driver.find_element(By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR,"input[id='country']").send_keys('Sri')
locator = (By.XPATH,"//a[text()='Srilanka']")
WebDriverWait(driver,10).until(visibility_of_element_located(locator))
driver.find_element(By.XPATH,"//a[text()='Srilanka']").click()
driver.find_element(By.CLASS_NAME,"checkbox.checkbox-primary").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
message= driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']").text
print(message)
assert "Success" in message