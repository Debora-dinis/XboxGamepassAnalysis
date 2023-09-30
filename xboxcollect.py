from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas


url = 'https://www.xbox.com/en-US/xbox-game-pass/games?xr=shellnav'

#options = webdriver.ChromeOptions()
#options.add_argument("--headless=new")
#driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()

driver.get(url)

button_increase_xpath = '//*[@id="unique-id-for-paglist-generated-select-menu-trigger"]'
click_button_by_xpath(driver, button_increase_xpath)

button_200_xpath = '//*[@id="unique-id-for-paglist-generated-select-menu-3"]'
click_button_by_xpath(driver, button_200_xpath)

platform_change_path = '//*[@id="filter-playon"]/div/button'

click_button_by_xpath(driver, platform_change_path)




"""games_dictionary = extract_games(driver)

print(str(len(games_dictionary)) + ' games added')

   

games_df = pandas.DataFrame.from_dict(games_dictionary)

games_df = pandas.DataFrame.transpose(games_df)



games_df.to_csv('xbox.csv')"""  