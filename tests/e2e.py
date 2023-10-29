
from utils.logger import get_logger
from utils.selenium_utils import load_path, get_selenium_driver, find_element, get_element_value

def get_chrome_driver (driver_type) :
    chrome_driver = get_selenium_driver("CHROME")
    if not (chrome_driver):
        get_logger().error('failed to load chrome driver')    
    return chrome_driver


def is_service_available(application_url):
    chrome = get_chrome_driver('')
    try : 
        app_url = "{application_url}/score".format(application_url=application_url)
        element_xpath = '/html/body/div/table'
        path = load_path(chrome,app_url)
        return find_element(path,element_xpath,4) 
    except : 
        return False


def validate_user_score_with_limits(application_url , user_name , low_limit , high_limit ):
    chrome = get_chrome_driver('')
    try : 
        app_url = "{application_url}/score?user_name={user_name}".format(application_url=application_url,user_name=user_name)
        path = load_path(chrome,app_url)
        element_xpath = '//*[@id="score"]'
        score = get_element_value(path,element_xpath,2) 
        return low_limit <= int(score) <= high_limit 
    except : 
        return False
    
    

def main(site_url,user_name,low_limit,high_limit):
    if validate_user_score_with_limits(site_url,user_name,low_limit,high_limit):
        return 0 
    else: 
        return -1
    
# main('http://localhost:30000','idubi',1,1000)



