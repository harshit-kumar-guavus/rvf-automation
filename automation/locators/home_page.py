from selenium.webdriver.common.by import By


class HomePage(object):
    SOURCES = (By.XPATH, "//ul[@class='nav navbar-nav']/li[3]/a[1]")
    CHARTS = (By.XPATH, "//ul[@class='nav navbar-nav']/li[4]/a[1]")
    DASHBOARDS = (By.XPATH, "//ul[@class='nav navbar-nav']/li[5]/a[1]")
    DATABASES_OPTION = (By.XPATH, "//li[@class='dropdown open']//li[1]//a[1]")
    TABLES_OPTION = (By.XPATH, "//li[@class='dropdown open']//li[5]//a[1]")