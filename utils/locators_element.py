from utils.waits import get_locator_type

class LocatorsElement:
    
    def get_element(element,type,locator):
        return element.find_element(get_locator_type(type),locator)
    
    def get_elements(element,type,locator):
        return element.find_elements(get_locator_type(type),locator)
