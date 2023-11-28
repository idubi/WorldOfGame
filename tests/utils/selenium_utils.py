from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FIREFOX_OPTIONS
from selenium.webdriver.chrome.options import Options as CHROME_OPTIONS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from utils.logger import get_logger
import time 

WEB_DRIVER_PATH_CHROME = './resources/selenium/chromedriver-win64/chromedriver.exe'
 
def get_selenium_driver(browser_type,flag_disable_extensions = False):
    try:
        if browser_type == "CHROME":
            options= CHROME_OPTIONS()
            options.add_argument("--incognito")
            options.add_argument("--lang=en-us")
            options.add_argument("--disable-web-security")
            options.add_argument("--allow-running-insecure-content")
            if flag_disable_extensions :
                options.add_argument("--disable-extensions")
                options.add_argument("--start-maximized")
            return webdriver.Chrome(service=Service(executable_path=WEB_DRIVER_PATH_CHROME), options=options)
        elif browser_type == "FIREFOX":
            options = FIREFOX_OPTIONS()
            options.binary_location = FIREFOX_PATH
            if flag_disable_extensions :
                options.set_preference("extensions.enabledAddons", "")
                options.add_argument("--start-maximized")
            return webdriver.Firefox(options=options)
    except Exception as ex:
        get_logger().error(f'error trying to set selenium driver : \n {ex.msg or ex}')
        return None


def load_path(driver, site):
    if driver:
        try :
            driver.get(site)
            status = driver.execute_script("return document.readyState")
            while not status=="complete":
                print(f'status of page is  {status}'  )
                time.sleep(0.3)
                status = driver.execute_script("return document.readyState")
                print(f'page loaded successfully  {driver}'  )
        except Exception as ex:
            get_logger().error(f'error trying to set load path : \n {ex.msg or ex}')
            return None
    return driver

def wait_before_find_element(driver, path , secconds,search_method='XPATH'):
    wait_for = WebDriverWait(driver,secconds)
    if search_method == 'ID': 
        element = wait_for.until(EC.presence_of_element_located((By.ID, path)))
    elif search_method == 'SELECTOR': 
        element = wait_for.until(EC.presence_of_element_located((By.CSS_SELECTOR, path)))
    elif search_method == 'CLASS_NAME' :
        element = wait_for.until(EC.presence_of_element_located((By.CLASS_NAME, path)))
    elif search_method == 'TAG' :
        element = wait_for.until(EC.presence_of_element_located((By.TAG_NAME, path)))
    else:
        element = wait_for.until(EC.presence_of_element_located((By.XPATH, path)))
    return element
        

def find_element(web_driver, path,wait_secconds,search_method='XPATH'):
    element= None
    if wait_secconds>0:
        element = wait_before_find_element(web_driver,path,wait_secconds,search_method)
    else:
        try:
            if search_method == 'ID': 
                element = web_driver.find_element(By.ID, path)
            elif search_method == 'SELECTOR': 
                element = web_driver.find_element(By.CSS_SELECTOR, path)
            elif search_method == 'CLASS_NAME' :
                element = web_driver.find_element(By.CLASS_NAME, path)
            elif search_method == 'TAG' :
                element = web_driver.find_element(By.TAG_NAME, path)
            else:
                element = web_driver.find_element(By.XPATH, path)
        except:
            get_logger().error(f'failed to get element , path={path} , search_method={search_method} ')           
    return element

def set_element_value(web_driver, path, value,wait_secconds=0.0):
    try:
        try:
            element = find_element(web_driver, path,wait_secconds)
            if element :
                element.send_keys(value)
                return True 
            raise Exception (f'set element value - element not found for path {path} ')               
        except: # Use JavaScript to set the value of the search box
            web_driver.execute_script(f"arguments[0].value='{value}';", element)  
            return True
    except Exception as ex:
        get_logger().error(f'error trying to set value of element in path {path} to {value} \n  {ex.msg or type(ex)}')
        return False

def click_element(web_driver, path,wait_secconds=0.0):
    try:
        element = find_element(web_driver, path,wait_secconds)
        if element :
            element.click() 
    except Exception as ex:
        get_logger().error(f'error trying to click element in path {path} \n {ex.msg or ex}')
        


def get_element_value(web_driver, path,wait_secconds=0.0):
    try:
        value = None
        element = find_element(web_driver, path,wait_secconds)
        if element:
            value = element.text or \
                    element.get_attribute("value") or \
                    element.get_attribute("innerText") or \
                    element.get_attribute("textContent")
        return value
    except Exception as ex:
        get_logger().error(f'error trying to get element value in path {path} \n {ex.msg or ex}')
        return value

def get_cookies(web_driver):
    site = web_driver.current_url
    if not site :
        get_logger().warning(f"site is not loaded to the web driver, cookies are only valid for specific site ")
        return False
    cookies = web_driver.get_cookies()
    
    if cookies :
        cookies_list = ''
        for cookie in cookies :
           cookies_list = cookies_list + cookie.get('name') +'=>' +  cookie.get('value') + '\n'
        get_logger().info(f"site ({site}) cookies  ==>  {cookies_list} ")
    else:
        get_logger().info(f'site ({site}) cookies  ==>  no cookies found')
    return cookies

def del_cookies(web_driver):
    site = web_driver.current_url
    if not site :
        get_logger().warning(f"site is not loaded to the web driver, cookies can be deleted for specific site ")
        return False
    web_driver.delete_all_cookies()
    return True
