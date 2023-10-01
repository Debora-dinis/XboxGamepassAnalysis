from utils.clickbypath import click_button_by_xpath


def set200games (driver):
    """
    Clicks on "games per page" button and set it to 200 games per page
        Parameters:
            driver: Selenium webdriver 
    """
    button_increase_xpath = '//*[@id="unique-id-for-paglist-generated-select-menu-trigger"]'
    click_button_by_xpath(driver, button_increase_xpath)

    button_200_xpath = '//*[@id="unique-id-for-paglist-generated-select-menu-3"]'
    click_button_by_xpath(driver, button_200_xpath)
