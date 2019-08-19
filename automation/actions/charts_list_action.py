from nimble.core.ui.utils.selenium_utils import SeleniumUtils
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys

from locators.charts_list_page import ChartsListPage


class ChartsListActions(object):
    def __init__(self, driver):
        self.selenium_utils = SeleniumUtils(driver)
        self.driver = driver

    def add_chart(self, chart_name):
        if ChartsListActions(self.driver).check_chart_present(chart_name) == 1:
            self.selenium_utils.click(ChartsListPage.DELETE_CHART_BUTTON)
            self.selenium_utils.click(ChartsListPage.CONFIRM_DELETE_OK)
        self.selenium_utils.click(ChartsListPage.ADD_CHART_ICON)

    def check_chart_present(self, chart_name):
        self.selenium_utils.click(ChartsListPage.FILTER_CHART_LIST_BTN)
        self.selenium_utils.click(ChartsListPage.FILTER_NAME_OPTION)
        self.selenium_utils.click(ChartsListPage.FILTER_ACTION)
        self.selenium_utils.fill_textbox(self.selenium_utils.find_element(*ChartsListPage.FILTER_ACTION_INPUT), "Equal To")
        self.selenium_utils.find_element(*ChartsListPage.FILTER_ACTION_INPUT).send_keys(Keys.RETURN)
        self.selenium_utils.fill_textbox(self.selenium_utils.find_element(*ChartsListPage.CHART_NAME_INPUT), chart_name)
        self.selenium_utils.click(ChartsListPage.SEARCH_BUTTON)
        try:
            print self.selenium_utils.wait_for_presence_of_element_located(ChartsListPage.CHART_NAME_FOUND, timeout=2)
            return 1
        except TimeoutException:
            return 0

