from utils.waits import Waits

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.waits = Waits(driver)

    def go_to_cart(self):
        try:
            self.waits.wait_and_click(
                'class',
                'shopping_cart_link'
            )
        except Exception as e:
            print(e)

    def go_to_checkout(self):
        try:
            self.waits.wait_and_click(
                'id',
                'checkout'
            )
        except Exception as e:
            print(e)