import json
from datetime import datetime

from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logs.testlogger import logger


def check_text(the_text):
    if any(ch.isdigit() for ch in the_text) or the_text.find("!") or the_text.find("|" or the_text.find(".")):
        return False
    else:
        return True


class BasePage:
    def __init__(self, browser, url, timeout=20):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self, timeout=13):
        self.browser.get(self.url)
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        self.browser.implicitly_wait(timeout)

    def element_exists(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            logger.error(f"{what} element is not presented")
            return False
        return self.browser.find_element(how, what)

    def has_proper_tag(self, how, what, tag):
        if self.element_exists(how, what).tag_name == tag:
            return True
        else:
            logger.error(f"The element {what} tag is {self.element_exists(how, what).tag_name}")
            return False

    def is_element_present(self, how, what):
        self.element_exists(how, what)
        return True

    def fill_the_input(self, how, what, key):
        self.element_exists(how, what)
        try:
            self.browser.find_element(how, what).send_keys(key)
        except ElementNotInteractableException:
            logger.error(f"The element {what} is not interactable")

    def click_the_button(self, how, what):
        self.element_exists(how, what)
        self.browser.find_element(how, what).click()

    def get_the_text(self, how, what):
        self.element_exists(how, what)
        try:
            text = self.browser.find_element(how, what).text
            return text
        except AttributeError:
            logger.error(f"{what} element is not presented")

    def check_the_text_between_tags(self, how, what):
        our_text = self.get_the_text(how, what)
        if check_text(our_text):
            pass
        else:
            logger.error(f"{what} element has another text: {self.get_the_text(how, what)}")
            return False

    def check_the_placeholder(self, how, what):
        our_text = self.element_exists(how, what).get_attribute('placeholder')
        if check_text(our_text):
            pass
        else:
            logger.error(f"{what} element has another text: {self.get_the_text(how, what)}")
            return False

    def check_the_attribute(self, how, what, attribute):
        try:
            self.element_exists(how, what).get_attribute(attribute)
            return self.element_exists(how, what).get_attribute(attribute)
        except AttributeError:
            logger.error(f"{what} element does not have attribute {attribute}")

    def check_the_property(self, how, what, attribute):
        try:
            self.element_exists(how, what).value_of_css_property(attribute)
            return self.element_exists(how, what).value_of_css_property(attribute)
        except AttributeError:
            logger.error(f"{what} element does not have attribute {attribute}")

    def make_screenshot(self, name):
        timing = str(datetime.now().strftime("_%d_%m_%y_%H-%M-%S"))
        logger.info(f"Screenshot has been captured at {datetime.now().isoformat()}")
        try:
            self.browser.save_screenshot(name + timing + ".jpg")
        except ModuleNotFoundError:
            logger.error("No module screenshot problem")
            return False
