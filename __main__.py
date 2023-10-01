# Import necessary libraries
from selenium import webdriver
import pandas
from gamesByFeature import extract_by_feature
from gamesByGenre import extract_by_genre
from gamesByPlatform import extract_by_platform
from utils.set200games import set200games
from xboxallgames import extract_games

# Define the URL to scrape
url = 'https://www.xbox.com/en-US/xbox-game-pass/games?xr=shellnav'

# Configure Chrome options for headless browsing and initialize the webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get(url)


# set games per page to 200
set200games(driver)

# extract all games
games_dictionary = extract_games(driver)
print(str(len(games_dictionary)) + ' games added')
games_df = pandas.DataFrame.from_dict(games_dictionary)
games_df = pandas.DataFrame.transpose(games_df)


# extract game IDs based on platform, genre, and features,
# and create corresponding databases to store this information.
platforms = extract_by_platform(driver)
genres = extract_by_genre(driver)
features = extract_by_feature(driver)


# populate the corresponding DataFrames with 1s and 0s
# to represent whether each game possesses the attribute or not.
platform_df = pandas.DataFrame(index=games_df['id'], columns=[
                               'xboxseries', 'xboxone', 'pc', 'cloud'])
genre_df = pandas.DataFrame(index=games_df['id'], columns=['action and adventure', 'classics', 'family and kids',
                            'indie', 'platformer', 'puzzle', 'role playing', 'shooter', 'simulation', 'sports', 'strategy'])
feature_df = pandas.DataFrame(index=games_df['id'], columns=[
                              'smart delivery', '4k', 'hdr', 'online multiplayer', 'local multiplayer', 'online co-op', 'local co-op'])
for game_id in games_df['id']:
    platform_df.loc[game_id, 'xboxseries'] =int(
        game_id in platforms['xboxseries'])
    platform_df.loc[game_id, 'xboxone'] =int(
        game_id in platforms['xboxone'])
    platform_df.loc[game_id, 'pc'] =int(
        game_id in platforms['pc'])
    platform_df.loc[game_id, 'cloud'] =int(
        game_id in platforms['cloud'])

    genre_df.loc[game_id, 'action and adventure'] =int(
        game_id in genres['action and adventure'])
    genre_df.loc[game_id, 'classics'] =int(
        game_id in genres['classics'])
    genre_df.loc[game_id, 'family and kids'] =int(
        game_id in genres['family and kids'])
    genre_df.loc[game_id, 'indie'] =int(
        game_id in genres['indie'])
    genre_df.loc[game_id, 'platformer'] =int(
        game_id in genres['platformer'])
    genre_df.loc[game_id, 'puzzle'] =int(
        game_id in genres['puzzle'])
    genre_df.loc[game_id, 'role playing'] =int(
        game_id in genres['role playing'])
    genre_df.loc[game_id, 'shooter'] =int(
        game_id in genres['shooter'])
    genre_df.loc[game_id, 'simulation'] =int(
        game_id in genres['simulation'])
    genre_df.loc[game_id, 'sports'] =int(
        game_id in genres['sports'])
    genre_df.loc[game_id, 'strategy'] =int(
        game_id in genres['strategy'])

    feature_df.loc[game_id, 'smart delivery'] =int(
        game_id in features['smart delivery'])
    feature_df.loc[game_id, '4k'] =int(
        game_id in features['4k'])
    feature_df.loc[game_id, 'hdr'] =int(
        game_id in features['hdr'])
    feature_df.loc[game_id, 'online multiplayer'] =int(
        game_id in features['online multiplayer'])
    feature_df.loc[game_id, 'local multiplayer'] =int(
        game_id in features['local multiplayer'])
    feature_df.loc[game_id, 'online co-op'] =int(
        game_id in features['online co-op'])
    feature_df.loc[game_id, 'local co-op'] =int(
        game_id in features['local co-op'])

# convert the diferent dataframes to csv
platform_df.to_csv('platforms.csv')
genre_df.to_csv('genres.csv')
feature_df.to_csv('features.csv')
games_df.to_csv('xbox.csv')
