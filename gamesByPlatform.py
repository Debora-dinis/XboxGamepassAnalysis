from utils.extractgamesid import extract_games_id


def extract_by_platform(driver):

    games_xboxseries = extract_games_id(
        driver, '//*[@id="filter-playon"]/div/button', '//*[@id="playonSelect"]/li[1]', True)
    print(str(len(games_xboxseries)) + ' games available on xbox series added')

    games_xboxone = extract_games_id(
        driver, '//*[@id="filter-playon"]/div/button', '//*[@id="playonSelect"]/li[2]', True)
    print(str(len(games_xboxone)) + ' games available on xbox one added')

    games_pc = extract_games_id(
        driver, '//*[@id="filter-playon"]/div/button', '//*[@id="playonSelect"]/li[3]', True)
    print(str(len(games_pc)) + ' games available on pc added')

    games_cloud = extract_games_id(
        driver, '//*[@id="filter-playon"]/div/button', '//*[@id="playonSelect"]/li[5]', True)
    print(str(len(games_cloud)) + ' games available on cloud added')

    return {'xboxseries': games_xboxseries,
            'xboxone': games_xboxone,
            'pc': games_pc,
            'cloud': games_cloud
            }
