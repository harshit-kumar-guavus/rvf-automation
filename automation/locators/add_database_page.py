from selenium.webdriver.common.by import By


class AddDatabasePage(object):
    DATABASE_NAME = (By.XPATH, "//input[@id='database_name']")
    SQL_ALCHEMY_URI = (By.XPATH, "//input[@id='sqlalchemy_uri']")
    TEST_CONNECTION_BUTTON = (By.XPATH, "//button[@id='testconn']")
    EXTRA = (By.XPATH, "//textarea[@id='extra']")
    SAVE_BUTTON = (By.XPATH, "//i[@class='fa fa-save']")