from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

firefox_profiles_path = os.environ['HOME'] + os.sep + 'Library/Application Support/Firefox/Profiles'

def webdriver_firefox():
    
    try:
        f = open(os.environ['HOME'] + os.sep + '.selenium_port', 'r')
        port = f.read()
        f.close()
        driver = webdriver.Remote(command_executor='http://127.0.0.1:%s/hub' % port, desired_capabilities=DesiredCapabilities.FIREFOX)
    except:
        default_profile = filter(lambda s: s.find('.selenium') >= 0, os.listdir(firefox_profiles_path))[0]
        profile = webdriver.FirefoxProfile(firefox_profiles_path + os.sep + default_profile)
        driver = webdriver.Firefox(profile)
        f = open(os.environ['HOME'] + os.sep + '.selenium_port', 'w')
        f.write(str(profile.port))
        f.close()
    return driver

def wait_until(func, timeout=3):
    print func
    while timeout > 0:
        if func(): return True
        time.sleep(0.1)
        timeout -= 0.1
        
    raise TimeoutException()
