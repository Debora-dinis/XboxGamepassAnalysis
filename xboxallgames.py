from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas

def extract_games(driver):
    games_dictionary= {}

    while True:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'm-product-placement-item')))

        all_games = driver.find_elements(By.CLASS_NAME, 'm-product-placement-item')

        for game in all_games:

            title_element = game.find_element(By.TAG_NAME, 'h3')
            title = title_element.text
            
            id = game.get_attribute('data-bigid')

            price = game.get_attribute('data-listprice')

            rating = game.get_attribute('data-ratingsystem')

            releasedate = game.get_attribute('data-releasedate')

            multiplayer = game.get_attribute('data-multiplayer')

            game_url_element = game.find_element(By.CSS_SELECTOR, 'a.gameDivLink')
            game_url = game_url_element.get_attribute('href')
            
            description = game.find_element(By.CLASS_NAME, 'popdescription').find_element(By.CLASS_NAME, 'furthcontent').get_attribute('innerHTML')

            game_dictionary = {
                'id': id,
                'price': price,
                'rating': rating,
                'releasedate': releasedate,
                'multiplayer': multiplayer,
                'url': game_url,
                'description': description,
            }

            games_dictionary[title] = game_dictionary
            print('game added')

        nextpage_path = '//*[@id="ContentBlockList_1"]/div[1]/div[2]/nav/ul/li[5]'
        
        if not click_button_by_xpath(driver, nextpage_path):
            break 
    return games_dictionary