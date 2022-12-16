from logs.testlogger import logger
from .global_variables import LINK
from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_auth_form_rows()
        self.should_be_main_url()

    def should_be_main_url(self):
        assert LINK in self.browser.current_url, "Main url is not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_auth_form_rows(self):
        assert self.is_element_present(*LoginPageLocators.LANGUAGE_BUTTONS), "language buttons are not presented"
        assert self.is_element_present(*LoginPageLocators.USER_INPUT), "User input is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT), "password input is not presented"
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD_LINK), "forgot password link is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "button input is not presented"

    def forms_should_have_proper_tags(self):
        assert self.has_proper_tag(*LoginPageLocators.USER_INPUT, "input"), "User tag is not an input"
        assert self.has_proper_tag(*LoginPageLocators.PASSWORD_INPUT, "input"), "Password tag is not an input"
        assert self.has_proper_tag(*LoginPageLocators.FORGOT_PASSWORD_LINK, "a"), "forgot password link is not a link"
        assert self.has_proper_tag(*LoginPageLocators.LOGIN_BUTTON, "button"), "login button is not a button"

    def switch_languages(self, language_name="en"):
        language = {"ru": LoginPageLocators.RUSSIAN,
                    "en": LoginPageLocators.ENGLISH,
                    "hi": LoginPageLocators.HINDI,
                    "ko": LoginPageLocators.KOREAN,
                    "ch": LoginPageLocators.CHINESE}
        self.click_the_button(*language[language_name])

    def fill_the_form(self, email, password):
        self.fill_the_input(*LoginPageLocators.USER_INPUT, email)
        self.fill_the_input(*LoginPageLocators.PASSWORD_INPUT, password)
        self.click_the_button(*LoginPageLocators.LOGIN_BUTTON)

    def restore_password(self, email, ok_text):
        self.click_the_button(*LoginPageLocators.FORGOT_PASSWORD_LINK)
        self.fill_the_input(*LoginPageLocators.PASSWORD_RESTORE_INPUT, email)
        self.click_the_button(*LoginPageLocators.PASSWORD_RESTORE_BUTTON)
        self.click_the_button(*LoginPageLocators.PASSWORD_RESTORE_BUTTON)
        assert self.is_element_present(*LoginPageLocators.PASSWORD_RESTORE_NOTE)
        assert self.is_element_present(*LoginPageLocators.PASSWORD_RESTORE_TEXT)
        note_text = self.get_the_text(*LoginPageLocators.PASSWORD_RESTORE_TEXT)
        assert note_text == ok_text
        self.click_the_button(*LoginPageLocators.PASSWORD_CLOSE_NOTIFICATION)

    def all_rows_have_proper_text(self):
        assert self.check_the_text_between_tags(*LoginPageLocators.USER_INPUT), "incorrect text"
        assert self.check_the_text_between_tags(*LoginPageLocators.PASSWORD_INPUT), "incorrect text"
        assert self.check_the_text_between_tags(*LoginPageLocators.FORGOT_PASSWORD_LINK), "incorrect text"

    def all_placeholders_have_proper_text(self):
        email_placeholder = self.element_exists(*LoginPageLocators.USER_INPUT).get_attribute('placeholder')
        password_placeholder = self.element_exists(*LoginPageLocators.PASSWORD_INPUT).get_attribute('placeholder')
        if email_placeholder != "Enter Email":
            logger.error(f"incorrect email_placeholder text: {email_placeholder}")
            raise AssertionError
        if password_placeholder != "Enter password":
            logger.error(f"incorrect password_placeholder text: {password_placeholder}")
            raise AssertionError

    def wrong_password(self):
        assert self.is_element_present(*LoginPageLocators.WRONG_PASS), "no notification about incorrect password"
        assert self.is_element_present(*LoginPageLocators.WRONG_PASS_TEXT), "no notification text"
        wrong_pass_text = self.get_the_text(*LoginPageLocators.WRONG_PASS_TEXT)
        self.click_the_button(*LoginPageLocators.CLOSE_WRONG_PASS)
        logger.warning(f"incorrect password, text: {wrong_pass_text}")
