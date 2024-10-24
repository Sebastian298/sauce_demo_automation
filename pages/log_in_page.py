from utils.waits import Waits

class LogIn:
    def __init__(self,driver):
        self.driver = driver
        self.waits = Waits(driver)

    def click_log_in(self):
        try:
            user_name_input = self.waits.wait_for_element("id","user-name")
            password_input = self.waits.wait_for_element("id","password")
            user_value = self.get_user_from_div()
            user_name_input.send_keys(user_value)
            password_value = self.get_password_from_div()
            password_input.send_keys(password_value)
            self.waits.wait_and_click("id","login-button")
        except Exception as e:
            print(e)

    def get_user_from_div(self):
        try:
            users_from_div = self.waits.wait_for_element("id","login_credentials")
            users_array = users_from_div.text.split('\n')
            return users_array[1]
        except Exception as e:
            print(e)

    def get_password_from_div(self):
        try:
            password_from_div = self.waits.wait_for_element("xpath",'//*[@id="root"]/div/div[2]/div[2]/div/div[2]')
            password_array = password_from_div.text.split('\n')
            return password_array[1]
        except Exception as e:
            print(e)