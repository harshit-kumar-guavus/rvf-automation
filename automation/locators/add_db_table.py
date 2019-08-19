from selenium.webdriver.common.by import By


class AddDBTable(object):
    DATABASE_NAME = (By.XPATH, "//a[@class='select2-choice']")
    SELECT_DB = (By.XPATH, "//input[@id='s2id_autogen1_search']")
    SCHEMA_NAME = (By.XPATH, "//input[@id='schema']")
    TABLE_NAME = (By.XPATH, "//input[@id='table_name']")
    SAVE_BUTTON = (By.XPATH, "//button[contains(@class,'btn-sm btn-primary')]")
