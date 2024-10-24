from selenium.webdriver.common.by import By

def get_locator_type(type):
    match type:
        case 'id':
            return By.ID
        
        case 'name':
            return By.NAME
        
        case 'xpath':
            return By.XPATH
        
        case 'css':
            return By.CSS_SELECTOR
        
        case 'class':
            return By.CLASS_NAME

        case _:
            return None