from nimble.core.ui.utils.selenium_utils import SeleniumUtils
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from locators.db_tables_list_page import DbTablesListPage


class DbTablesListActions(object):
    def __init__(self, driver):
        self.selenium_utils = SeleniumUtils(driver)
        self.driver = driver

    def add_db_table(self, table_name):
        if DbTablesListActions(self.driver).check_table_present(table_name) == 1:
            self.selenium_utils.click(DbTablesListPage.DELETE_TABLE_BUTTON)
            self.selenium_utils.click(DbTablesListPage.CONFIRM_DELETE_OK)
        self.selenium_utils.click(DbTablesListPage.ADD_TABLE_BUTTON)

    def check_table_present(self, table_name):
        self.selenium_utils.click(DbTablesListPage.CLOSE_SQL_LAB_FILTER)
        self.selenium_utils.click(DbTablesListPage.FILTER_BUTTON)
        self.selenium_utils.click(DbTablesListPage.FILTER_TABLE_NAME_OPTION)
        self.selenium_utils.click(DbTablesListPage.FILTER_ACTION)
        self.selenium_utils.fill_textbox(self.selenium_utils.find_element(*DbTablesListPage.FILTER_ACTION_INPUT), "Equal To")
        self.selenium_utils.find_element(*DbTablesListPage.FILTER_ACTION_INPUT).send_keys(Keys.RETURN)
        self.selenium_utils.fill_textbox(self.selenium_utils.find_element(*DbTablesListPage.TABLE_NAME_INPUT), table_name)
        self.selenium_utils.click(DbTablesListPage.SEARCH_BUTTON)
        try:
            self.selenium_utils.wait_for_presence_of_element_located(DbTablesListPage.TABLE_NAME_FOUND, 2000)
            return 1
        except NoSuchElementException:
            return 0

    def check_table_creation_msg(self):
        self.selenium_utils.wait_for_visibility_of_element_located(DbTablesListPage.ALERT_DIV)
        msg = self.selenium_utils.find_element(*DbTablesListPage.ALERT_DIV).text
        return msg

