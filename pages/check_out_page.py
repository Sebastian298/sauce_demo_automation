from utils.waits import Waits

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.waits = Waits(driver)

    def fill_checkout_form(self,first_name,last_name,postal_code):
        try:
            self.waits.wait_and_send_keys('id','first-name',first_name)
            self.waits.wait_and_send_keys('id','last-name',last_name)
            self.waits.wait_and_send_keys('id','postal-code',postal_code)
        except Exception as e:
            print(e)

    def go_to_checkout_overview(self):
        try:
            self.waits.wait_and_click(
                'id',
                'continue'
            )
        except Exception as e:
            print(e)

    def finish_checkout(self):
        try:
            self.waits.wait_and_click(
                'id',
                'finish'
            )
        except Exception as e:
            print(e)

    def get_checkout_complete_message(self):
        try:
            return self.waits.wait_for_element_to_be_visible('class','complete-header').text
        except Exception as e:
            print(e)

    def navigate_home(self):
        try:
            self.waits.wait_and_click(
                'id',
                'back-to-products'
            )
        except Exception as e:
            print(e)