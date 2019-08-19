from nimble.core.ui.utils.selenium_utils import SeleniumUtils

from actions.add_database_action import AddDatabaseActions
from actions.add_db_table_action import AddDbTableActions
from actions.charts_list_action import ChartsListActions
from actions.create_chart_action import CreateChartActions
from actions.databases_list_action import DatabasesListActions
from actions.db_tables_list_action import DbTablesListActions
from actions.generic_viz_action import GenericVizActions
from actions.homepage_action import HomePageActions
from actions.login_action import LoginActions


class CentralUtils(object):
    def __init__(self, driver):
        self.selenium_utils = SeleniumUtils(driver)
        self.driver = driver
        self.login_actions = LoginActions(self.driver)
        self.homepage_actions = HomePageActions(self.driver)
        self.database_list_actions = DatabasesListActions(self.driver)
        self.add_database_actions = AddDatabaseActions(self.driver)
        self.db_tables_list_actions = DbTablesListActions(self.driver)
        self.add_db_table_actions = AddDbTableActions(self.driver)
        self.charts_list_actions = ChartsListActions(self.driver)
        self.create_chart_actions = CreateChartActions(self.driver)
        self.generic_slice_actions = GenericVizActions(self.driver)

    def launch_and_login(self, username, password):
        self.login_actions.open_browser()
        self.login_actions.login(username, password)

    def add_database(self, database_name, sql_alchemy_uri, extras):
        self.homepage_actions.click_sources()
        self.homepage_actions.select_database_option()
        self.database_list_actions.click_add_database_icon()
        self.add_database_actions.add_database_details(database_name, sql_alchemy_uri, extras)

    def add_table(self, database_name, schema_name, table_name):
        self.homepage_actions.click_sources()
        self.homepage_actions.select_tables_option()
        self.db_tables_list_actions.add_db_table(table_name)
        self.add_db_table_actions.add_table_details(database_name, schema_name, table_name)
        assert "The table was created" in self.db_tables_list_actions.check_table_creation_msg()
        assert self.db_tables_list_actions.check_table_present(table_name) == 1

    def create_new_chart(self, data_source_name, chart_name, column_name, row_limit):
        self.homepage_actions.click_charts()
        self.charts_list_actions.add_chart(chart_name)
        self.create_chart_actions.create_new_chart(data_source_name)
        self.generic_slice_actions.remove_time_range_filter()
        self.generic_slice_actions.select_columns_not_group_by(column_name)
        self.generic_slice_actions.select_row_limit_not_group_by(row_limit)
        self.generic_slice_actions.save_chart(chart_name)
        self.homepage_actions.click_charts()
        assert self.charts_list_actions.check_chart_present(chart_name) == 1
