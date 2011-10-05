from selenium import webdriver
from selenium.webdriver.common.exceptions import TimeoutException
from selenium.webdriver.firefox.extensionconnection import ExtensionConnection
import time

def webdriver_firefox():
    try:
#        driver = webdriver.Remote(command_executor=ExtensionConnection(),
#                                       browser_name='firefox', platform='ANY', version='',
#                                       javascript_enabled=True)
        driver = webdriver.Remote(command_executor='http://localhost:7055/hub')
    except:
        profile = webdriver.FirefoxProfile('selenium')
        driver = webdriver.Firefox(profile)
    return driver

def wait_until(func, timeout=3):
    print func
    while timeout > 0:
        if func(): return True
        time.sleep(0.1)
        timeout -= 0.1
        
    raise TimeoutException()