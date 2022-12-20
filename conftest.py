import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FFOptions
from msedge.selenium_tools import Edge
from msedge.selenium_tools import EdgeOptions
from logs.testlogger import logger
from pages.global_variables import AUTH_LINK
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage


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
                     help="Choose browser: chrome, edge or firefox")


@pytest.fixture(scope="class")
def browser(request):
    logger.info('Test has started')
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart Chrome browser for test...")
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


@pytest.fixture(params=[('username1@name.ru', 'pass1'), ('username2@name.ru', 'pass2'),
                        ('username3@name.ru', 'pass3'), ('username4@name.ru', 'pass4'),
                        ], ids=["username1", "username2", "username3",  "username4"])
def user_pass(request):
    return request.param


@pytest.fixture(params=['en', 'ru', 'hi',
                        pytest.param('ch', marks=pytest.mark.xfail(reason='ch payment button doesnt react')),
                        pytest.param(6, marks=pytest.mark.xfail(reason='ko auth failed')), ],
                        ids=['en', 'ru', 'hi', 'ch', 'ko'])
def language(request):
    return request.param


@pytest.fixture
def top_up_page(browser, user_pass, language):
    with allure.step("Authorization"):
        login_page = LoginPage(browser, AUTH_LINK)
        login_page.open()
        login_page.switch_languages(language)
        login_page.should_be_login_page()
        user, password = user_pass[0], user_pass[1]
        login_page.fill_the_form(user, password)
        payment_page = PaymentPage(browser, browser.current_url)
        payment_page.open()
    return payment_page

