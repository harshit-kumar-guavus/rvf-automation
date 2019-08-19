from nimble.core.ui.utils.selenium_utils import SeleniumUtils

from locators.login_page import LoginPage


class LoginActions(object):
    def __init__(self, driver):
        self.selenium_utils = SeleniumUtils(driver)
        self.driver = driver

    def open_browser(self):
        self.driver.get("http://rvf.lab.guavus.com:8888/")
        self.driver.maximize_window()

    def login(self, username, password):
        self.selenium_utils.fill_textbox(
            self.selenium_utils.wait_for_visibility_of_element_located(LoginPage.USERNAME), username)
        self.selenium_utils.fill_textbox(self.selenium_utils.find_element(*LoginPage.PASSWORD), password)
        self.selenium_utils.click(LoginPage.SUBMIT_BUTTON)
