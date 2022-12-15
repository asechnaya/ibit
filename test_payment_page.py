import allure
import pytest
from parametrization import Parametrization

from pages.global_variables import LINK, PREFIX, PASSWORD, USER
from pages.payment_page import PaymentPage
from pages.login_page import LoginPage


@allure.feature("Payment feature")
@allure.story("user should be able to top up his balance")
@allure.title('Base design features check')
@Parametrization.parameters('user_email', 'user_password')
@Parametrization.case('username1', 'username1@name.ru', 'pass1')
@Parametrization.case('username2', 'username2@name.ru', 'pass2')
@Parametrization.case('username3', 'username3@name.ru', 'pass3')
@Parametrization.case('username4', 'username4@name.ru', 'pass4')
class TestPaymentPage:
    def test_design_of_payments(self, browser, user_email, user_password):
        with allure.step("Login as user"):
            browser.delete_all_cookies()
            authorization_link = PREFIX + USER + ":" + PASSWORD + "@" + LINK
            login_page = LoginPage(browser, authorization_link)
            login_page.open()
            login_page.should_be_login_page()
            login_page.switch_languages("en")
            login_page.fill_the_form(user_email, user_password)
            payment_page = PaymentPage(browser, browser.current_url)

        with allure.step("Testing payment page design"):
            payment_page.should_be_payment_page()
            payment_page.should_be_all_statuses()
            payment_page.should_be_payment_system_choice()
            payment_page.should_be_currency_and_amount_choice()

        with allure.step("Testing privileges and bonuses links"):
            payment_page.should_be_description_of_privileges_text()
            payment_page.should_be_description_of_bonuses_text()

    @Parametrization.parameters('status_name')
    @Parametrization.case('vip', 'vip')
    @Parametrization.case('gold', 'gold')
    @Parametrization.case('silver', 'silver')
    @Parametrization.case('mini', 'mini')
    def test_switching_statuses(self, browser, user_email, user_password, status_name):
        with allure.step("Open a new page"):
            browser.delete_all_cookies()
            authorization_link = PREFIX + USER + ":" + PASSWORD + "@" + LINK
            login_page = LoginPage(browser, authorization_link)
            login_page.open()
            login_page.should_be_login_page()

        with allure.step("Trying to log in as a user"):
            login_page.fill_the_form(user_email, user_password)
            payment_page = PaymentPage(browser, browser.current_url)

        with allure.step("Testing payment page"):
            payment_page.should_be_payment_url()
            payment_page.unselect_bonus(False)
            payment_page.click_on_status_item(status_name)
            payment_page.bar_is_according_status(status_name)


@pytest.mark.smoke
@allure.feature("Payment feature")
@allure.story("user should be able to top up his balance")
@allure.title('Base design features check')
class TestPayments:
    def test_basic_payment(self, browser):
        with allure.step("Authorization"):
            browser.delete_all_cookies()
            authorization_link = PREFIX + USER + ":" + PASSWORD + "@" + LINK
            login_page = LoginPage(browser, authorization_link)
            login_page.open()
            login_page.switch_languages()
            login_page.should_be_login_page()
            login_page.fill_the_form('username1@name.ru', 'pass1')
            payment_page = PaymentPage(browser, browser.current_url)

        with allure.step("Testing payment"):
            payment_page.should_be_payment_url()
            payment_page.unselect_bonus(False)
            payment_page.make_payment()

    @pytest.mark.skip(reason="critical bugs with ch payment and ko auth")
    @Parametrization.parameters('language_name')
    @Parametrization.case('en', 'en')
    @Parametrization.case('ru', 'ru')
    @Parametrization.case('hi', 'hi')
    @Parametrization.case('ch', 'ch')
    @Parametrization.case('ko', 'ko')
    def test_different_languages_payment(self, browser, language_name):
        with allure.step("Authorization"):
            browser.delete_all_cookies()
            authorization_link = PREFIX + USER + ":" + PASSWORD + "@" + LINK
            login_page = LoginPage(browser, authorization_link)
            login_page.open()
            login_page.switch_languages(language_name)
            login_page.should_be_login_page()
            login_page.fill_the_form('username1@name.ru', 'pass1')
            payment_page = PaymentPage(browser, browser.current_url)

        with allure.step(f"Testing payment for language = {language_name}"):
            payment_page.should_be_payment_url()
            payment_page.unselect_bonus(False)
            payment_page.make_payment(language_name)

    def test_manual_payment_with_different_currencies(self, browser):
        with allure.step("Authorization"):
            browser.delete_all_cookies()
            authorization_link = PREFIX + USER + ":" + PASSWORD + "@" + LINK
            login_page = LoginPage(browser, authorization_link)
            login_page.open()
            login_page.switch_languages()
            login_page.should_be_login_page()
            login_page.fill_the_form('username1@name.ru', 'pass1')
            payment_page = PaymentPage(browser, browser.current_url)
            payment_page.should_be_payment_url()
        for cur in ["ru", "en", "ch"]:
            with allure.step(f"Testing manual payment, currency = {cur}"):
                payment_page.select_currency(cur)
                payment_page.manually_enter_amount(502)
                payment_page.unselect_bonus(True)
                payment_page.make_payment()
