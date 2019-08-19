from selenium.webdriver.common.by import By


class LoginPage(object):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='signIn']")