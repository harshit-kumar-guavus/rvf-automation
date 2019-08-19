from selenium.webdriver.common.by import By


class ChartsListPage(object):
    FILTER_CHART_LIST_BTN = (By.XPATH, "//button[@class='btn btn-default dropdown-toggle']")
    FILTER_NAME_OPTION = (By.XPATH, "//a[@name='slice_name']")
    FILTER_ACTION = (By.XPATH, "//a[@class='select2-choice']")
    FILTER_ACTION_INPUT = (By.XPATH, "//input[@id='s2id_autogen2_search']")
    CHART_NAME_INPUT = (By.XPATH, "//input[@id='slice_name']")
    SEARCH_BUTTON = (By.XPATH, "//button[@id='search-action']")
    NO_RECORDS_FOUND_LABEL = (By.XPATH, "//b[contains(text(),'No records found')]")
    CHART_NAME_FOUND = (By.XPATH, "//div[@class='table-responsive']//td[3]")
    DELETE_CHART_BUTTON = (By.XPATH, "//i[@class='fa fa-eraser']")
    CONFIRM_DELETE_OK = (By.XPATH, "//a[@id='modal-confirm-ok']")
    ADD_CHART_ICON = (By.XPATH, "//i[@class='fa fa-plus']")
