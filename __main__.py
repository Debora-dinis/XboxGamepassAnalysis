from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas
from gamesByFeature import extract_by_feature
from gamesByGenre import extract_by_genre
from gamesByPlatform import extract_by_platform

from utils.clickbypath import click_button_by_xpath
from utils.extractgamesid import extract_games_id
from utils.set200games import set200games
from xboxallgames import extract_games


url = 'https://www.xbox.com/en-US/xbox-game-pass/games?xr=shellnav'

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

driver.get(url)

set200games(driver)

games_dictionary = extract_games(driver)

print(str(len(games_dictionary)) + ' games added')


games_df = pandas.DataFrame.from_dict(games_dictionary)

games_df = pandas.DataFrame.transpose(games_df)

games_df.to_csv('xbox.csv')


platforms = extract_by_platform(driver)
genres = extract_by_genre(driver)
features = extract_by_feature(driver)

platform_df = pandas.DataFrame(index=games_df['id'], columns=[
                               'xboxseries', 'xboxone', 'pc', 'cloud'])
genre_df = pandas.DataFrame(index=games_df['id'], columns=['action and adventure', 'classics', 'family and kids',
                            'indie', 'platformer', 'puzzle', 'role playing', 'shooter', 'simulation', 'sports', 'strategy'])
feature_df = pandas.DataFrame(index=games_df['id'], columns=[
                              'smart delivery', '4k', 'hdr', 'online multiplayer', 'local multiplayer', 'online co-op', 'local co-op'])

for game_id in games_df['id']:
    platform_df.loc[game_id, 'xboxseries'] = 1 if (
        game_id in platforms['xboxseries']) else 0
    platform_df.loc[game_id, 'xboxone'] = 1 if (
        game_id in platforms['xboxone']) else 0
    platform_df.loc[game_id, 'pc'] = 1 if (game_id in platforms['pc']) else 0
    platform_df.loc[game_id, 'cloud'] = 1 if (
        game_id in platforms['cloud']) else 0

    genre_df.loc[game_id, 'action and adventure'] = 1 if (
        game_id in genres['action and adventure']) else 0
    genre_df.loc[game_id, 'classics'] = 1 if (
        game_id in genres['classics']) else 0
    genre_df.loc[game_id, 'family and kids'] = 1 if (
        game_id in genres['family and kids']) else 0
    genre_df.loc[game_id, 'indie'] = 1 if (game_id in genres['indie']) else 0
    genre_df.loc[game_id, 'platformer'] = 1 if (
        game_id in genres['platformer']) else 0
    genre_df.loc[game_id, 'puzzle'] = 1 if (game_id in genres['puzzle']) else 0
    genre_df.loc[game_id, 'role playing'] = 1 if (
        game_id in genres['role playing']) else 0
    genre_df.loc[game_id, 'shooter'] = 1 if (
        game_id in genres['shooter']) else 0
    genre_df.loc[game_id, 'simulation'] = 1 if (
        game_id in genres['simulation']) else 0
    genre_df.loc[game_id, 'sports'] = 1 if (game_id in genres['sports']) else 0
    genre_df.loc[game_id, 'strategy'] = 1 if (
        game_id in genres['strategy']) else 0

    feature_df.loc[game_id, 'smart delivery'] = 1 if (
        game_id in features['smart delivery']) else 0
    feature_df.loc[game_id, '4k'] = 1 if (game_id in features['4k']) else 0
    feature_df.loc[game_id, 'hdr'] = 1 if (game_id in features['hdr']) else 0
    feature_df.loc[game_id, 'online multiplayer'] = 1 if (
        game_id in features['online multiplayer']) else 0
    feature_df.loc[game_id, 'local multiplayer'] = 1 if (
        game_id in features['local multiplayer']) else 0
    feature_df.loc[game_id,
                   'online co-op'] = 1 if (game_id in features['online co-op']) else 0
    feature_df.loc[game_id,
                   'local co-op'] = 1 if (game_id in features['local co-op']) else 0


platform_df.to_csv('platforms.csv')
genre_df.to_csv('genres.csv')
feature_df.to_csv('features.csv')
