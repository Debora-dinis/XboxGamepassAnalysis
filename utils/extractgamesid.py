from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.clickbypath import click_button_by_class, click_button_by_xpath


def extract_games_id(driver, path1, path2,first):
    platform_games = []
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'm-product-placement-item')))
    if not first:
        click_button_by_xpath(driver, path1)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, path2)))
    click_button_by_xpath(driver, path2)

    while True:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'm-product-placement-item')))

        all_games = driver.find_elements(By.CLASS_NAME, 'm-product-placement-item')

        for game in all_games:
            
            id = game.get_attribute('data-bigid')

            platform_games.append(id)
        
                        
        nextpage_class = 'paginatenext'
        
        if not click_button_by_class(driver, nextpage_class):
            break 

    click_button_by_xpath(driver, path2)
    return platform_games