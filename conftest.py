import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FFOptions
from msedge.selenium_tools import Edge
from msedge.selenium_tools import EdgeOptions
from logs.testlogger import logger


def headless_chrome():
    ops = Options()
    ops.add_argument("--headless")
    driver = webdriver.Chrome(options=ops)
    return driver


def headless_firefox():
    ops = FFOptions()
    ops.add_argument("--headless")
    driver = webdriver.Firefox(options=ops)
    return driver


def headless_edge():
    # make Edge headless
    edge_options = EdgeOptions()
    edge_options.use_chromium = True  # if we miss this line, we can't make Edge headless
    edge_options.add_argument('headless')
    edge_options.add_argument('disable-gpu')
    driver = Edge(options=edge_options)
    return driver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="class")
def browser(request):
    logger.info('Test has started')
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test...")
        browser = headless_chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test...")
        browser = headless_firefox()
    elif browser_name == "edge":
        print("\nstart edge browser for test...")
        browser = headless_edge()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.delete_all_cookies()
    yield browser
    print("\nquit browser..")
    browser.quit()
    logger.info('Test has finished')

