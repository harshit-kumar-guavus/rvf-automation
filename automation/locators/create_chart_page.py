from selenium.webdriver.common.by import By


class CreateChartPage(object):
    CHOOSE_DATA_SOURCE = (By.XPATH, "//div[@class='Select-placeholder']")
    DATA_SOURCE_INPUT = (By.XPATH, "//div[@class='Select-input']//input")
    CHOOSE_VIZ = (By.XPATH, "//span[@class='label label-default']")
    CREATE_CHART_BTN = (By.XPATH, "//button[@class='btn btn-primary']")
