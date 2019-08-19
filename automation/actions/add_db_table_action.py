from nimble.core.ui.utils.selenium_utils import SeleniumUtils
from selenium.webdriver.common.keys import Keys

from locators.add_db_table import AddDBTable


class AddDbTableActions(object):
    def __init__(self, driver):
        self.selenium_utils = SeleniumUtils(driver)
        self.driver = driver

    def add_table_details(self, database_name, schema_name, table_name):
        self.selenium_utils.click(AddDBTable.DATABASE_NAME)
        self.selenium_utils.fill_textbox(self.selenium_utils.find_element(*AddDBTable.SELECT_DB), database_name)
        self.selenium_utils.find_element(*AddDBTable.SELECT_DB).send_keys(Keys.RETURN)
        self.selenium_utils.fill_textbox(self.selenium_utils.find_element(*AddDBTable.SCHEMA_NAME), schema_name)
        self.selenium_utils.fill_textbox(self.selenium_utils.find_element(*AddDBTable.TABLE_NAME), table_name)
        self.selenium_utils.click(AddDBTable.SAVE_BUTTON)

