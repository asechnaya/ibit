import allure
import pytest
import requests
from parametrization import Parametrization
from selenium.common import exceptions

from logs.testlogger import logging
from pages.global_variables import LINK, OK_TEXT, NOT_OK_TEXT, PASSWORD, PREFIX, USER
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage


logger = logging.getLogger('test login page')


@allure.feature("Login feature")
@allure.story("user should be able to login to top up his balance")
@allure.title('Base design features check')
@allure.testcase("https://st.scrdairy.com/", "Разработка автотестов для главной страницы")
@Parametrization.parameters('language')
@Parametrization.case('english', "en")
@Parametrization.case('chinese', "ch")
@Parametrization.case('korean',  "ko")
@Parametrization.case('russian', "ru")
@Parametrization.case('hindi',   "hi")
class TestLoginPagePositiveCases:
    @Parametrization.parameters('user_email', 'user_password')
    @Parametrization.case('username1', 'username1@name.ru', 'pass1')
    @Parametrization.case('username2', 'username2@name.ru', 'pass2')
    @Parametrization.case('username3', 'username3@name.ru', 'pass3')
    @Parametrization.case('username4', 'username4@name.ru', 'pass4')
    def test_registered_emails(self, browser, language, user_email, user_password):
        with allure.step("Open a new page"):
            browser.delete_all_cookies()
            authorization_link = PREFIX + USER + ":" + PASSWORD + "@" + LINK
            login_page = LoginPage(browser, authorization_link)
            login_page.open()
            login_page.should_be_login_page()
            login_page.switch_languages(language)

        with allure.step("Trying to log in as 4 different users"):
            login_page.fill_the_form(user_email, user_password)
            payment_page = PaymentPage(browser, browser.current_url)
            payment_page.should_be_payment_url()
            browser.back()

    @pytest.mark.xfail(run=True)
    def test_restore_password_for_registered(self, browser, language):
        with allure.step("Open a new page"):
            browser.delete_all_cookies()
            authorization_link = PREFIX + USER + ":" + PASSWORD + "@" + LINK
            login_page = LoginPage(browser, authorization_link)
            login_page.open()
            login_page.should_be_login_page()
            login_page.switch_languages(language)

        with allure.step("Trying to log in as 4 different users"):
            login_page.restore_password('username1@name.ru', OK_TEXT[language])
            browser.back()

    @pytest.mark.xfail(run=True)
    def test_design_is_correct(self, browser, language):
        with allure.step("Open a new page"):
            browser.delete_all_cookies()
            authorization_link = PREFIX + USER + ":" + PASSWORD + "@" + LINK
            login_page = LoginPage(browser, authorization_link)
            login_page.open()
            login_page.should_be_login_page()
            login_page.switch_languages(language)

        with allure.step("Tags are correct"):
            logger.info("test the design")
            login_page.forms_should_have_proper_tags()

        with allure.step("all titles are correct"):
            login_page.all_rows_have_proper_text()

        with allure.step("Placeholders are correct"):
            login_page.all_placeholders_have_proper_text()


@allure.feature("Login feature")
@allure.story("user should be able to login to top up his balance")
@allure.title('Negative cases for login page')
@pytest.mark.login
class TestLoginPageNegativeCases:
    @pytest.mark.xfail(raises=exceptions.InvalidArgumentException, run=True)
    def test_status_code_random_authorization(self, browser):
        with allure.step("Open a new page without auth"):
            browser.delete_all_cookies()
            login_page = LoginPage(browser, PREFIX + "randomname:password@" + LINK)
            login_page.open()
            login_page.should_be_login_page()
            pytest.xfail("auth is not correct")

    def test_random_authorization(self):
        with allure.step("Open a new page with random auth"):
            status_code = requests.get(PREFIX + "random:random@" + LINK).status_code
            logger.info("page status_code is ", status_code)
            assert status_code == 401

    def test_unregistered_emails(self, browser):
        with allure.step("Open a new page"):
            browser.delete_all_cookies()
            authorization_link = PREFIX + USER + ":" + PASSWORD + "@" + LINK
            login_page = LoginPage(browser, authorization_link)
            login_page.open()
            login_page.should_be_login_page()

        with allure.step("Trying to log in as random users"):
            login_page.fill_the_form("user_email@email.ru", "user_password")
            payment_page = PaymentPage(browser, browser.current_url)
            payment_page.should_be_payment_url()
            browser.back()

    @pytest.mark.xfail(run=False)
    def test_restore_password_for_unregistered(self, browser):
        with allure.step("Open a new page"):
            browser.delete_all_cookies()
            authorization_link = PREFIX + USER + ":" + PASSWORD + "@" + LINK
            login_page = LoginPage(browser, authorization_link)
            login_page.open()
            login_page.should_be_login_page()

        with allure.step("Trying to log in as 4 different users"):
            login_page.restore_password('username500@name.ru', NOT_OK_TEXT)
            pytest.xfail("Email is not checked")
            browser.back()
