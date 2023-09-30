from utils.extractgamesid import extract_games_id


def extract_by_genre(driver):
    games_action_adventure = extract_games_id(
        driver, '//*[@id="filter-genre"]/div/button', '//*[@id="genreSelect"]/li[1]', False)
    print(str(len(games_action_adventure)) + ' action and adventure games added')

    games_classics = extract_games_id(
        driver, '//*[@id="filter-genre"]/div/button', '//*[@id="genreSelect"]/li[2]', True)
    print(str(len(games_classics)) + ' classic games added')

    games_family_kids = extract_games_id(
        driver, '//*[@id="filter-genre"]/div/button', '//*[@id="genreSelect"]/li[3]', True)
    print(str(len(games_family_kids)) + ' family and kids games added')

    games_indie = extract_games_id(
        driver, '//*[@id="filter-genre"]/div/button', '//*[@id="genreSelect"]/li[4]', True)
    print(str(len(games_indie)) + ' indie games added')

    games_platformer = extract_games_id(
        driver, '//*[@id="filter-genre"]/div/button', '//*[@id="genreSelect"]/li[5]', True)
    print(str(len(games_platformer)) + ' platformer games added')

    games_puzzle = extract_games_id(
        driver, '//*[@id="filter-genre"]/div/button', '//*[@id="genreSelect"]/li[6]', True)
    print(str(len(games_puzzle)) + ' puzzle games added')

    games_role_playing = extract_games_id(
        driver, '//*[@id="filter-genre"]/div/button', '//*[@id="genreSelect"]/li[7]', True)
    print(str(len(games_role_playing)) + ' role playing games added')

    games_shooter = extract_games_id(
        driver, '//*[@id="filter-genre"]/div/button', '//*[@id="genreSelect"]/li[8]', True)
    print(str(len(games_shooter)) + ' shooter games added')

    games_simulation = extract_games_id(
        driver, '//*[@id="filter-genre"]/div/button', '//*[@id="genreSelect"]/li[9]', True)
    print(str(len(games_simulation)) + ' simulation games added')

    games_sports = extract_games_id(
        driver, '//*[@id="filter-genre"]/div/button', '//*[@id="genreSelect"]/li[10]', True)
    print(str(len(games_sports)) + ' sports games added')

    games_strategy = extract_games_id(
        driver, '//*[@id="filter-genre"]/div/button', '//*[@id="genreSelect"]/li[11]', True)
    print(str(len(games_strategy)) + ' strategy games added')

    return {'action and adventure' : games_action_adventure,
            'classics' : games_classics,
            'family and kids' : games_family_kids,
            'indie': games_indie,
            'platformer' : games_platformer,
            'puzzle' : games_puzzle,
            'role playing' : games_role_playing,
            'shooter' : games_shooter,
            'simulation' : games_simulation,
            'sports' : games_sports,
            'strategy' : games_strategy}
