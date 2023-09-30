import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract_games_id(driver, path):
    platform_games = []
    click_button_by_xpath(driver, path)

    while True:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'm-product-placement-item')))

        all_games = driver.find_elements(By.CLASS_NAME, 'm-product-placement-item')

        for game in all_games:
            
            id = game.get_attribute('data-bigid')

            platform_games = platform_games.append(id)
        

        nextpage_path = '//*[@id="ContentBlockList_1"]/div[1]/div[2]/nav/ul/li[5]'
        
        if not click_button_by_xpath(driver, nextpage_path):
            break 
    return games_dictionary