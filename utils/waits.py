from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.get_locator_type import get_locator_type
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException,ElementClickInterceptedException

class Waits:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, type, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((get_locator_type(type), locator))
            )
            return element
        except NoSuchElementException:
            raise NoSuchElementException(f"Element with {type} = {locator} not found")
        except TimeoutException:
            raise TimeoutException(f"Element with {type} = {locator} not found within {time} seconds")
        
    def wait_for_element_to_be_clickable(self, type, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable((get_locator_type(type), locator))
            )
            return element
        except NoSuchElementException:
            raise NoSuchElementException(f"Element with {type} = {locator} not found")
        except TimeoutException:
            raise TimeoutException(f"Element with {type} = {locator} not found within {time} seconds")
        except ElementClickInterceptedException:
            raise ElementClickInterceptedException(f"Element with {type} = {locator} not clickable")
        
    def wait_for_element_to_be_visible(self, type, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located((get_locator_type(type), locator))
            )
            return element
        except NoSuchElementException:
            raise NoSuchElementException(f"Element with {type} = {locator} not found")
        except TimeoutException:
            raise TimeoutException(f"Element with {type} = {locator} not found within {time} seconds")
        except ElementNotVisibleException:
            raise ElementNotVisibleException(f"Element with {type} = {locator} not visible")
        
    def wait_and_click(self, type, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable((get_locator_type(type), locator))
            )
            element.click()
        except NoSuchElementException:
            raise NoSuchElementException(f"Element with {type} = {locator} not found")
        except TimeoutException:
            raise TimeoutException(f"Element with {type} = {locator} not found within {time} seconds")
        except ElementClickInterceptedException:
            raise ElementClickInterceptedException(f"Element with {type} = {locator} not clickable")
        
    def get_elements_in_parent(self, parent_type, parent_locator, child_type, child_locator, time=10):
        try:
            parent_element = self.wait_for_element(parent_type, parent_locator, time)
            elements = parent_element.find_elements(get_locator_type(child_type), child_locator)
            return elements
        except NoSuchElementException:
            raise NoSuchElementException(f"Element with {parent_type} = {parent_locator} not found")
        except TimeoutException:
            raise TimeoutException(f"Element with {parent_type} = {parent_locator} not found within {time} seconds")
        
    def wait_and_send_keys(self, type, locator, text, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable((get_locator_type(type), locator))
            )
            element.send_keys(text)
        except NoSuchElementException:
            raise NoSuchElementException(f"Element with {type} = {locator} not found")
        except TimeoutException:
            raise TimeoutException(f"Element with {type} = {locator} not found within {time} seconds")
        except ElementClickInterceptedException:
            raise ElementClickInterceptedException(f"Element with {type} = {locator} not clickable")