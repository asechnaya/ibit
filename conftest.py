import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from logs.testlogger import logger
from pages.base_page import BasePage
from pages.global_variables import LINK, PASSWORD, PREFIX, USER


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="class")
def browser(request):
    logger.info('Test has started')
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        options = Options()
        print("\nstart chrome browser for test...")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test...")
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
    logger.info('Test has finished')


@pytest.fixture(scope="class")
def authorization(browser):
    browser.delete_all_cookies()
    authorization_link = PREFIX + USER + ":" + PASSWORD + "@" + LINK
    page = BasePage(browser, authorization_link)
    page.open()
