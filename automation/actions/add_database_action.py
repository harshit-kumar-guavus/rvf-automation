import time

from nimble.core.ui.utils.selenium_utils import SeleniumUtils
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.add_database_page import AddDatabasePage


class AddDatabaseActions(object):
    def __init__(self, driver):
        self.selenium_utils = SeleniumUtils(driver)
        self.driver = driver

    def add_database_details(self, database_name, sql_alchemy_uri, extra):
        self.selenium_utils.fill_textbox(
            self.selenium_utils.wait_for_visibility_of_element_located(AddDatabasePage.DATABASE_NAME), database_name)
        self.selenium_utils.fill_textbox(self.selenium_utils.find_element(*AddDatabasePage.SQL_ALCHEMY_URI), sql_alchemy_uri)
        if extra:
            self.selenium_utils.scroll_into_view(self.selenium_utils.find_element(*AddDatabasePage.SAVE_BUTTON))
            self.selenium_utils.fill_textbox(self.selenium_utils.find_element(*AddDatabasePage.EXTRA), extra)
        self.selenium_utils.scroll_into_view(self.selenium_utils.find_element(*AddDatabasePage.DATABASE_NAME))
        self.selenium_utils.click(AddDatabasePage.TEST_CONNECTION_BUTTON)
        msg = AddDatabaseActions(self.driver).get_alert_message()
        assert "Seems OK" in msg
        self.selenium_utils.scroll_into_view(self.selenium_utils.find_element(*AddDatabasePage.SAVE_BUTTON))
        self.selenium_utils.click(AddDatabasePage.SAVE_BUTTON)
        time.sleep(5)

    def get_alert_message(self):
        msg = ""
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(), 'Timed out waiting for alert')
            alert = self.driver.switch_to.alert
            msg = alert.text
            alert.accept()
        except TimeoutException:
            print("no alert")
        return msg
