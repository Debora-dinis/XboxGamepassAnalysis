from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_button_by_xpath(driver, xpath):
    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button = driver.find_element(By.XPATH, xpath)
        button.click()
        return True
    except Exception as e:
        print('Button not found')
        return False
    
def click_button_by_class(driver, classname):
    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, classname)))
        button = driver.find_element(By.CLASS_NAME, classname)
        button.click()
        return True
    except Exception as e:
        print('Button not found')
        return False
    
