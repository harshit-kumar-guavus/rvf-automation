from nimble.core.ui.utils.selenium_utils import SeleniumUtils

from locators.database_list_page import DatabasesListPage


class DatabasesListActions(object):
    def __init__(self, driver):
        self.selenium_utils = SeleniumUtils(driver)
        self.driver = driver

    def click_add_database_icon(self):
        self.selenium_utils.click(DatabasesListPage.ADD_DB_BUTTON)