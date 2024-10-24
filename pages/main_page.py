from utils.waits import Waits
from utils.locators_element import LocatorsElement as Locators

class MainPage:
    def __init__(self,driver):
        self.driver = driver
        self.waits = Waits(driver)

    def add_items_to_cart(self):
        try:
            self.waits.wait_for_element_to_be_visible('xpath','/html/body/div/div/div/div[1]/div[1]/div[2]/div')
            products_list = self.waits.get_elements_in_parent('id','inventory_container','class','inventory_item')
            for product_element in products_list:
                add_to_cart_button = Locators.get_element(product_element,'class','btn_inventory')
                add_to_cart_button.click()
        except Exception as e:
            print(e)

    def go_to_menu_options(self):
        try:
            self.waits.wait_and_click(
                'id',
                'react-burger-menu-btn'
            )
        except Exception as e:
            print(e)

    def go_to_logout(self):
        try:
            self.waits.wait_and_click(
                'id',
                'logout_sidebar_link'
            )
        except Exception as e:
            print(e)