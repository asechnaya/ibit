import logging

import allure
import pytest

from pages.global_variables import PAYSYS


@allure.feature("Payment feature")
@allure.story("user should be able to top up his balance")
@allure.title('Base design features check')
@allure.testcase("https://ibitcy.com/interview/qa/mobile-deposit/#/payment", "Payment page tests")
class TestPaymentPageDesign:
    @pytest.mark.xfail(reason="design is not fully established. No status description")
    def test_design_of_payments(self, top_up_page):
        with allure.step("Testing payment page design"):
            top_up_page.should_be_payment_page()
            top_up_page.should_be_all_statuses()
            top_up_page.should_be_payment_system_choice()
            top_up_page.should_be_currency_and_amount_choice()

        with allure.step("Testing privileges and bonuses links"):
            top_up_page.should_be_description_of_privileges_text()  # this is absent
            top_up_page.should_be_description_of_bonuses_text()

    @pytest.mark.parametrize("status_name", ['vip', 'gold', 'silver', 'mini'])
    def test_switching_statuses(self, top_up_page, status_name):
        with allure.step(f"Switch to status {status_name}"):
            top_up_page.should_be_payment_url()
            top_up_page.unselect_bonus(False)
            top_up_page.click_on_status_item(status_name)
            top_up_page.bar_is_according_status(status_name)


@pytest.mark.smoke
@allure.feature("Payment feature")
@allure.story("user should be able to top up his balance")
@allure.title('Base payment features check')
class TestPayments:

    attempts = [1, 2]

    def test_basic_payment(self, top_up_page, language):
        with allure.step("Testing payment"):
            top_up_page.should_be_payment_url()
            top_up_page.unselect_bonus(False)
            top_up_page.make_payment()

        with allure.step(f"Testing payment for language = {language}"):
            top_up_page.should_be_payment_url()
            top_up_page.unselect_bonus(False)
            top_up_page.make_payment(language)

    def test_manual_payment_with_different_currencies(self, top_up_page):
        for cur in ["ru", "en", "ch"]:
            with allure.step(f"Testing manual payment, currency = {cur}"):
                top_up_page.select_currency(cur)
                top_up_page.manually_enter_amount(502)
                top_up_page.unselect_bonus(True)
                top_up_page.make_payment()

    @pytest.mark.parametrize("ps_number", [1, 2, 3, 4,
                                           pytest.param(5, marks=pytest.mark.xfail(reason='bug: alert')),
                                           pytest.param(6, marks=pytest.mark.xfail(reason='bug: alert')),
                                           7, 8, 9, 10, 11, 12, 14],
                             ids=['VISA, MasterCard, Maestro', 'VISA, MasterCard, Visa Electron',
                                  'VISA, MasterCard, Maestro', 'VISA, MasterCard (2)', 'Skrill', 'Neteller',
                                  'Perfect Money', 'Fasapay', 'Payweb', 'WebMoney', 'UnionPay', 'UnionPay 2',
                                  'Yandex.Money'])
    def test_payment_with_different_ps(self, top_up_page, ps_number):
        with allure.step(f"Testing manual payment, payment_system = {PAYSYS[ps_number]}"):
            top_up_page.select_ps(ps_number)
            top_up_page.make_payment()

    @pytest.mark.xfail(reason="The second attempt always fails")
    def test_payment_with_qiwi(self, top_up_page):
        with allure.step("Testing manual payment, payment_system=QIWI"):
            top_up_page.select_ps(13)
            for i in self.attempts:
                logging.info(f"Qiwi payment number {i}")
                top_up_page.enter_phone_and_make_payment()
