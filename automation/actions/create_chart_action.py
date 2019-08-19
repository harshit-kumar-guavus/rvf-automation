from nimble.core.ui.utils.selenium_utils import SeleniumUtils
from selenium.webdriver.common.keys import Keys

from locators.create_chart_page import CreateChartPage


class CreateChartActions(object):
    def __init__(self, driver):
        self.selenium_utils = SeleniumUtils(driver)
        self.driver = driver

    def create_new_chart(self, data_source_name, viz_type="table"):
        self.selenium_utils.click(CreateChartPage.CHOOSE_DATA_SOURCE)
        self.selenium_utils.find_element(*CreateChartPage.DATA_SOURCE_INPUT).send_keys(data_source_name)
        self.selenium_utils.find_element(*CreateChartPage.DATA_SOURCE_INPUT).send_keys(Keys.RETURN)
        self.selenium_utils.click(CreateChartPage.CREATE_CHART_BTN)

