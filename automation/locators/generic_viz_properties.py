from selenium.webdriver.common.by import By


class GenericVizProperties(object):
    RUN_QUERY_BUTTON = (By.XPATH, "//button[@class='query btn btn-sm btn-default']")
    SAVE_BUTTON = (By.XPATH, "//button[@class='btn btn-sm btn-default']")
    DATA_SOURCE_EXPANDER = (By.XPATH, "//div[@id='controlSections-pane-query']/div[1]/div[1]/div[1]/a[1]/i[1]")
    PUBLICATION_EXPANDER = (By.XPATH, "//div[@id='controlSections-pane-query']/div[2]/div[1]/div[1]/a[1]/i[1]")
    SUBSCRIPTION_EXPANDER = (By.XPATH, "//div[@id='controlSections-pane-query']/div[3]/div[1]/div[1]/a[1]/i[1]")
    ADVANCED_OPTIONS_EXPANDER = (By.XPATH, "//div[@id='controlSections-pane-query']/div[4]/div[1]/div[1]/a[1]/i[1]")
    TIME_EXPANDER = (By.XPATH, "//div[@id='controlSections-pane-query']/div[5]/div[1]/div[1]/a[1]/i[1]")
    GROUP_BY_EXPANDER = (By.XPATH, "//div[@id='controlSections-pane-query']/div[6]/div[1]/div[1]/a[1]/i[1]")

    TIME_RANGE_EDIT = (By.XPATH, "//div[@data-test='time_range']//span[@class='label label-default']")
    TIME_RANGE_NO_FILTER_OPTION = (By.XPATH, "//label[contains(text(),'No filter')]")
    TIME_RANGE_OK_BTN = (By.XPATH, "//button[@class='float-right ok btn btn-sm btn-primary']")
    NOT_GROUP_BY_COLUMNS = (By.XPATH, "//span[@id='react-select-11--value']//div[@class='Select-placeholder']")
    NOT_GROUP_BY_COLUMNS_INPUT = (By.XPATH, "//span[@id='react-select-11--value']//div[@class='Select-input']//input")
    NOT_GROUP_BY_ROW_LIMIT = (By.XPATH, "//span[@id='react-select-13--value']//div[@class='Select-value']")
    NOT_GROUP_BY_ROW_LIMIT_INPUT = (By.XPATH, "//span[@id='react-select-13--value']//div[@class='Select-input']//input")
    SAVE_CHART_MODAL = (By.XPATH, "//div[@class='modal-large modal-dialog']//div[@class='modal-header']")
    SAVE_AS_CHART_NAME = (By.XPATH, "//input[@placeholder='[chart name]']")
    SAVE_CHART_MODAL_BTN = (By.XPATH, "//button[@id='btn_modal_save']")
