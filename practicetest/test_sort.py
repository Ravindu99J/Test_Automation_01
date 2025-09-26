from selenium import webdriver
from selenium.webdriver.common.by import By



def test_sort(browserInstance):

    driver = browserInstance
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')
    driver.find_element(By.XPATH,"//th/span[text()='Veg/fruit name']").click()


    names= driver.find_elements(By.XPATH,"//tr/td[1]")
    original_list= []
    for name in names:
        original_list.append(name.text)
    copy_list= original_list

    print(copy_list)
    sorted_list= sorted(original_list)
    print(sorted_list)
    assert original_list == sorted_list
