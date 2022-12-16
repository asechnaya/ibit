import allure
import pytest
from parametrization import Parametrization

from pages.global_variables import AUTH_LINK, PAYSYS
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
class TestPaymentPageDesign:
    @pytest.mark.xfail(reason="design is not fully established. No status description")
    def test_design_of_payments(self, browser, user_email, user_password):
        with allure.step("Login as user"):
            login_page = LoginPage(browser, AUTH_LINK)
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
            payment_page.should_be_description_of_privileges_text()  # this is absent
            payment_page.should_be_description_of_bonuses_text()

    @Parametrization.parameters('status_name')
    @Parametrization.case('vip', 'vip')
    @Parametrization.case('gold', 'gold')
    @Parametrization.case('silver', 'silver')
    @Parametrization.case('mini', 'mini')
    def test_switching_statuses(self, browser, user_email, user_password, status_name):
        with allure.step("Open a new page"):
            login_page = LoginPage(browser, AUTH_LINK)
            login_page.open()
            login_page.should_be_login_page()

        with allure.step("Trying to log in as a user"):
            login_page.fill_the_form(user_email, user_password)
            payment_page = PaymentPage(browser, browser.current_url)

        with allure.step(f"Switch to status {status_name}"):
            payment_page.should_be_payment_url()
            payment_page.unselect_bonus(False)
            payment_page.click_on_status_item(status_name)
            payment_page.bar_is_according_status(status_name)


@pytest.mark.smoke
@allure.feature("Payment feature")
@allure.story("user should be able to top up his balance")
@allure.title('Base design features check')
class TestPayments:

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    def test_basic_payment(self, browser):
        with allure.step("Authorization"):
            login_page = LoginPage(browser, AUTH_LINK)
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
            login_page = LoginPage(browser, AUTH_LINK)
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
            login_page = LoginPage(browser, AUTH_LINK)
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

    @pytest.mark.parametrize("ps_number", my_list)
    def test_payment_with_different_ps(self, browser, ps_number):
        with allure.step("Proceed Authorization"):
            login_page = LoginPage(browser, AUTH_LINK)
            login_page.open()
            login_page.switch_languages()
            login_page.should_be_login_page()
            login_page.fill_the_form('username1@name.ru', 'pass1')
            payment_page = PaymentPage(browser, browser.current_url)
            payment_page.should_be_payment_url()

        with allure.step(f"Testing manual payment, payment_system = {PAYSYS[ps_number]}"):
            payment_page.select_ps(ps_number)
            payment_page.make_payment()

    def test_payment_with_qiwi(self, browser):
        with allure.step("Authorization"):
            login_page = LoginPage(browser, AUTH_LINK)
            login_page.open()
            login_page.switch_languages()
            login_page.should_be_login_page()
            login_page.fill_the_form('username1@name.ru', 'pass1')
            payment_page = PaymentPage(browser, browser.current_url)
            payment_page.should_be_payment_url()

        with allure.step(f"Testing manual payment, payment_system = QIWI"):
            payment_page.select_ps(13)
            payment_page.enter_phone_and_make_payment()

