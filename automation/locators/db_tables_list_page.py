from selenium.webdriver.common.by import By


class DbTablesListPage(object):
    ALERT_DIV = (By.XPATH, "//div[@id='alert-container']")
    FILTER_BUTTON = (By.XPATH, "//button[@class='btn btn-default dropdown-toggle']")
    FILTER_TABLE_NAME_OPTION = (By.XPATH, "//a[@name='table_name']")
    CLOSE_SQL_LAB_FILTER = (By.XPATH, "//a[@class='btn remove-filter']")
    FILTER_ACTION = (By.XPATH, "//a[@class='select2-choice']")
    FILTER_ACTION_INPUT = (By.XPATH, "//input[@id='s2id_autogen4_search']")
    TABLE_NAME_INPUT = (By.XPATH, "//input[@id='table_name']")
    SEARCH_BUTTON = (By.XPATH, "//button[@id='search-action']")
    NO_RECORDS_FOUND_LABEL = (By.XPATH, "//b[contains(text(),'No records found')]")
    TABLE_NAME_FOUND = (By.XPATH, "//div[@class='table-responsive']//td[3]")
    DELETE_TABLE_BUTTON = (By.XPATH, "//i[@class='fa fa-eraser']")
    CONFIRM_DELETE_OK = (By.XPATH, "//a[@id='modal-confirm-ok']")
    ADD_TABLE_BUTTON = (By.XPATH, "//i[@class='fa fa-plus']")
