import json

import pytest

from pageObjects.login import LoginPage

test_data_path = '../Data/test_practiceData.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data['Data']


@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):

    driver = browserInstance
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shop_page = loginPage.login(test_list_item['username'], test_list_item['password'])
    shop_page.add_product_to_cart(test_list_item['product_name'])
    print(shop_page.getTitle())
    checkout_confirmation = shop_page.goto_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address('Srilanka')
    checkout_confirmation.validate_order()
