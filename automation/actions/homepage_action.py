from nimble.core.ui.utils.selenium_utils import SeleniumUtils

from locators.home_page import HomePage


class HomePageActions(object):
    def __init__(self, driver):
        self.selenium_utils = SeleniumUtils(driver)
        self.driver = driver

    def click_sources(self):
        self.selenium_utils.click(HomePage.SOURCES)

    def click_charts(self):
        self.selenium_utils.click(HomePage.CHARTS)

    def click_dashboard(self):
        self.selenium_utils.click(HomePage.DASHBOARDS)

    def select_database_option(self):
        self.selenium_utils.click(HomePage.DATABASES_OPTION)

    def select_tables_option(self):
        self.selenium_utils.click(HomePage.TABLES_OPTION)
