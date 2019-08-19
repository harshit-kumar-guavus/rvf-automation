import time

from nimble.core.ui.utils.selenium_utils import SeleniumUtils
from selenium.webdriver.common.keys import Keys

from locators.generic_viz_properties import GenericVizProperties


class GenericVizActions(object):
    def __init__(self, driver):
        self.selenium_utils = SeleniumUtils(driver)
        self.driver = driver

    def remove_time_range_filter(self):
        self.selenium_utils.click_through_js(self.selenium_utils.find_element(*GenericVizProperties.DATA_SOURCE_EXPANDER))
        self.selenium_utils.click_through_js(self.selenium_utils.find_element(*GenericVizProperties.PUBLICATION_EXPANDER))
        self.selenium_utils.click_through_js(self.selenium_utils.find_element(*GenericVizProperties.SUBSCRIPTION_EXPANDER))
        self.selenium_utils.click_through_js(self.selenium_utils.find_element(*GenericVizProperties.ADVANCED_OPTIONS_EXPANDER))
        time.sleep(2)
        self.selenium_utils.click(GenericVizProperties.TIME_RANGE_EDIT)
        self.selenium_utils.click(GenericVizProperties.TIME_RANGE_NO_FILTER_OPTION)
        self.selenium_utils.click(GenericVizProperties.TIME_RANGE_OK_BTN)
        self.selenium_utils.click(GenericVizProperties.TIME_EXPANDER)

    def select_columns_not_group_by(self, column_name):
        time.sleep(2)
        self.selenium_utils.click(GenericVizProperties.GROUP_BY_EXPANDER)
        time.sleep(1)
        self.selenium_utils.click(GenericVizProperties.NOT_GROUP_BY_COLUMNS)
        self.selenium_utils.fill_textbox(self.selenium_utils.find_element(*GenericVizProperties.NOT_GROUP_BY_COLUMNS_INPUT), column_name)
        self.selenium_utils.find_element(*GenericVizProperties.NOT_GROUP_BY_COLUMNS_INPUT).send_keys(Keys.RETURN)

    def select_row_limit_not_group_by(self, row_limit):
        time.sleep(2)
        self.selenium_utils.click(GenericVizProperties.NOT_GROUP_BY_ROW_LIMIT)
        self.selenium_utils.fill_textbox(self.selenium_utils.find_element(*GenericVizProperties.NOT_GROUP_BY_ROW_LIMIT_INPUT), row_limit)
        self.selenium_utils.find_element(*GenericVizProperties.NOT_GROUP_BY_ROW_LIMIT_INPUT).send_keys(Keys.RETURN)

    def run_query(self):
        self.selenium_utils.scroll_into_view(self.selenium_utils.find_element(*GenericVizProperties.RUN_QUERY_BUTTON))
        self.selenium_utils.click(GenericVizProperties.RUN_QUERY_BUTTON)
        time.sleep(7)

    def save_chart(self, chart_name):
        self.selenium_utils.scroll_into_view(self.selenium_utils.find_element(*GenericVizProperties.SAVE_BUTTON))
        self.selenium_utils.click(GenericVizProperties.SAVE_BUTTON)
        self.selenium_utils.wait_for_visibility_of_element_located(GenericVizProperties.SAVE_CHART_MODAL)
        self.selenium_utils.fill_textbox(self.selenium_utils.find_element(*GenericVizProperties.SAVE_AS_CHART_NAME), chart_name)
        self.selenium_utils.click(GenericVizProperties.SAVE_CHART_MODAL_BTN)
        time.sleep(7)
