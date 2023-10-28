
from utils.logger import get_logger
from selenium.webdriver.common.keys import Keys
from utils.selenium_utils import load_path, get_selenium_driver, find_element, get_element_value
    


def get_chrome_driver (driver_type) :
    chrome_driver = get_selenium_driver(driver_type or "CHROME")
    if not (chrome_driver):
        get_logger().error('failed to load chrome driver')    
    return chrome_driver


def is_service_available(application_url):
    chrome = get_chrome_driver('')
    try : 
        path = load_path(chrome,application_url)
        if find_element(path,'/html/body/div/table',4) :
            return True
        else :
            return False
    except : 
        return False



def main(site_url):
    if is_service_available(site_url):
        return 0 
    else: 
        return 1
    
# main('http://localhost:30000/score')



