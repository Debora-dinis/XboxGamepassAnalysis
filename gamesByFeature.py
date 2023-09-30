from utils.extractgamesid import extract_games_id


def extract_by_feature(driver):
    games_smart_delivery = extract_games_id(
        driver, '//*[@id="filter-features"]/div/button', '//*[@id="featureSelect"]/li[1]', False)
    print(str(len(games_smart_delivery)) + ' games with smart delivery added')

    games_4k = extract_games_id(
        driver, '//*[@id="filter-features"]/div/button', '//*[@id="featureSelect"]/li[2]', True)
    print(str(len(games_4k)) + ' games with 4k added')

    games_hdr = extract_games_id(
        driver, '//*[@id="filter-features"]/div/button', '//*[@id="featureSelect"]/li[3]', True)
    print(str(len(games_hdr)) + ' games with hdr added')

    games_online_multiplayer = extract_games_id(
        driver, '//*[@id="filter-features"]/div/button', '//*[@id="featureSelect"]/li[4]', True)
    print(str(len(games_online_multiplayer)) + ' games with online multiplayer added')

    games_local_multiplayer = extract_games_id(
        driver, '//*[@id="filter-features"]/div/button', '//*[@id="featureSelect"]/li[5]', True)
    print(str(len(games_local_multiplayer)) + ' games with local multiplayer added')

    games_online_co_op = extract_games_id(
        driver, '//*[@id="filter-features"]/div/button', '//*[@id="featureSelect"]/li[6]', True)
    print(str(len(games_online_co_op)) + ' games with online co-op added')

    games_local_co_op = extract_games_id(
        driver, '//*[@id="filter-features"]/div/button', '//*[@id="featureSelect"]/li[7]', True)
    print(str(len(games_local_co_op)) + ' games with local co-op added')

    return {
        'smart delivery' : games_smart_delivery,
        '4k' : games_4k,
        'hdr' : games_hdr,
        'online multiplayer' : games_online_multiplayer,
        'local multiplayer' : games_local_multiplayer,
        'online co-op' : games_online_co_op,
        'local co-op' : games_local_co_op
    }
