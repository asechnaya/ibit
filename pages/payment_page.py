import time

from logs.testlogger import logger
from utils.money_converters import currency_converter
from .base_page import BasePage
from .global_variables import BAR_COLOR, BAR_LOCATOR, FINAL_TEXT
from .locators import FinalPageLocators, PaymentPageLocators, ps_set


class PaymentPage(BasePage):
    def should_be_payment_page(self):
        self.should_be_payment_url()
        self.should_be_payment_box()
        self.should_be_title()
        self.should_be_bonus_link()
        self.should_be_total_amount()

    def should_be_payment_url(self):
        assert 'payment' in self.browser.current_url, "payment url is not found"

    def should_be_payment_box(self):
        assert self.is_element_present(*PaymentPageLocators.PAYMENT_BOX), 'Payment choice is not presented'

    def should_be_title(self):
        assert self.is_element_present(*PaymentPageLocators.TITLE), 'Title link is not presented'

    def should_be_total_amount(self):
        assert self.is_element_present(*PaymentPageLocators.TOTAL_AMOUNT), 'total amount is not presented'

    def should_be_description_of_privileges_text(self):
        # Check is the link is correct and there is a description
        self.click_the_button(*PaymentPageLocators.TITLE)
        assert '#/pricing?' not in self.browser.current_url, \
            'No description of status privileges program conditions '

    def should_be_bonus_link(self):
        assert self.is_element_present(*PaymentPageLocators.BONUS), "BONUS link is not presented"

    def should_be_description_of_bonuses_text(self):
        # Check is the link is correct and there is a description
        self.click_the_button(*PaymentPageLocators.BONUS)
        assert '#/pricing?' not in self.browser.current_url, \
            'No description of bonus program conditions '

    def should_be_all_statuses(self):
        assert self.is_element_present(*PaymentPageLocators.ITEM_VIP), "VIP status is not presented"
        assert self.is_element_present(*PaymentPageLocators.ITEM_GOLD), "GOLD status is not presented"
        assert self.is_element_present(*PaymentPageLocators.ITEM_SILVER), "SILVER status is not presented"
        assert self.is_element_present(*PaymentPageLocators.ITEM_MINI), "MINI status is not presented"

    def should_be_payment_system_choice(self):
        assert self.is_element_present(*PaymentPageLocators.PAYMENT_FIELD), "No choice of payment systems"
        assert self.get_the_text(*PaymentPageLocators.PAYMENT_FIELD) == "VISA, MasterCard, Maestro", \
            "No payment description"

    def should_be_currency_and_amount_choice(self):
        assert self.is_element_present(*PaymentPageLocators.CURRENCY), "No choice of currencies"
        assert self.is_element_present(*PaymentPageLocators.AMOUNT), "No amount input"

    def should_be_proceed_button(self):
        assert self.is_element_present(*PaymentPageLocators.PROCEED), "No proceed_button"

    def click_on_status_item(self, item):
        item_locator = {"vip": PaymentPageLocators.ITEM_VIP,
                        "gold": PaymentPageLocators.ITEM_GOLD,
                        "silver": PaymentPageLocators.ITEM_SILVER,
                        "mini": PaymentPageLocators.ITEM_MINI}
        self.click_the_button(*item_locator[item]), "Item is not clickable"
        status_item = self.element_exists(*PaymentPageLocators.STATUS_ITEM)
        logger.info(f"status active item {item} is {status_item.get_attribute('active')}")
        assert status_item.get_attribute("active") == item, "Item is not illuminated"

    def make_payment(self):
        self.click_the_button(*PaymentPageLocators.PROCEED)

    def payment_should_be_successful(self, language: str = "en"):
        assert self.get_the_text(*FinalPageLocators.PROCESSING_TEXT) == FINAL_TEXT[language]
        self.click_the_button(*FinalPageLocators.BACK_LINK)

    def bar_is_according_status(self, attribute: str):
        current_bar_index = self.check_the_attribute(*PaymentPageLocators.BAR, "style")
        current_bar_color = self.check_the_property(*PaymentPageLocators.BAR, "background-color")
        assert current_bar_index == BAR_LOCATOR[attribute], "Bar width is not correct"
        assert current_bar_color == BAR_COLOR[attribute], "Bar color is not correct"
        logger.info(f"status active item is {attribute}, bar's color is {BAR_COLOR[attribute]}")

    def total_amount_is_correct(self, status: str = "gold", currency: str = "en", bonus: bool = True):
        """
        this function asserts text in the box with expected calculated sum for a status
        """
        amount = currency_converter(currency, bonus)
        expected_text = str(amount[status])
        amount_text = self.get_the_text(*PaymentPageLocators.TOTAL_AMOUNT)
        logger.info(f"total_amount_is_correct ({amount_text}) = {expected_text})")
        assert amount_text == f"${expected_text}"

    def select_bonus(self, ischecked=False):
        """

        :param ischecked: is True, then checkbox is selected. If ischecked is False then it should be unselected
        """
        checkbox = self.check_the_attribute(*PaymentPageLocators.BONUS_CHECKBOX, "checked")
        print(checkbox)
        if checkbox == ischecked:
            pass
        else:
            self.is_element_present(*PaymentPageLocators.BONUS_CHECKBOX)
            self.click_the_button(*PaymentPageLocators.BONUS_CHECKBOX)
        logger.info(f"checkbox is {ischecked}")

    def manually_enter_amount(self, amount):
        # Find a checkbox
        self.fill_the_input(*PaymentPageLocators.AMOUNT, amount)

    def select_currency(self, cur):
        # List of currencies:
        currency = {"ru": PaymentPageLocators.CURRENCY_RU,
                    "en": PaymentPageLocators.CURRENCY_US,
                    "ch": PaymentPageLocators.CURRENCY_CH}
        # select currencies list
        self.click_the_button(*PaymentPageLocators.CURRENCY)
        # select one of currencies
        self.click_the_button(*currency[cur])

    def select_ps(self, num: int = 1):
        # Select list of payments
        self.click_the_button(*PaymentPageLocators.PAYMENT_FIELD)
        # Select one of payment systems
        payment_sys_number = ps_set(num)
        self.click_the_button(*payment_sys_number)

    def enter_phone_and_make_payment(self, number: str = " 912 345-23-12"):
        self.click_the_button(*PaymentPageLocators.PROCEED)
        # input_number
        self.click_the_button(*FinalPageLocators.PHONE)
        self.fill_the_input(*FinalPageLocators.PHONE, number)
        time.sleep(1)
        self.click_the_button(*FinalPageLocators.PHONE_PROCEED)
