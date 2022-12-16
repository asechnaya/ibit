from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_OUT_BUTTON = (By.CLASS_NAME, "btn-profile")
    LOGIN_OUT_ICON = (By.CLASS_NAME, "icon.icon-sign-out")
    LOGIN_OUT_TEXT = (By.XPATH, "//div[6]")
    SEARCH_INPUT = (By.CSS_SELECTOR, ".txt-search")
    COW_NUMBER = (By.CSS_SELECTOR, "div.search-results-types > ul > li:nth-child(1) > span > span > span:nth-child(3)")


def ps_set(num):
    return By.CSS_SELECTOR, f"payment-system-selector > div > div.select > rg-select > ul > li:nth-child({num})"


class PaymentPageLocators:
    PAYMENT_BOX = (By.CLASS_NAME, "page")
    TITLE = (By.LINK_TEXT, "Status privileges description")
    BONUS = (By.LINK_TEXT, "Bonus")
    ITEM_VIP = (By.NAME, "vip")
    ITEM_GOLD = (By.NAME, "gold")
    ITEM_SILVER = (By.NAME, "silver")
    ITEM_MINI = (By.NAME, "mini")
    STATUS_ITEM = (By.CSS_SELECTOR, "status-selector > div.status-selector > div:nth-child(1) > status-item")
    BAR = (By.CSS_SELECTOR, "indicator > div > div > div.bar > div.ghost")
    PAYMENT_CAPTION = (By.CSS_SELECTOR, "#riot-app > div > payment-system-selector > div > div.field-title")
    PAYMENT_FIELD = (By.CSS_SELECTOR, "payment-system-selector > div > div.select > rg-select > div > div > span.title")
    CURRENCY = (By.CSS_SELECTOR, ".current > .title:nth-child(1)")
    CURRENCY_RU = By.CSS_SELECTOR, ".active > .item:nth-child(3)"
    CURRENCY_US = (By.CSS_SELECTOR, "div.currency > div > rg-select > ul > li:nth-child(2) > span")
    CURRENCY_CH = (By.CSS_SELECTOR, "div.currency > div > rg-select > ul > li:nth-child(3)")
    AMOUNT = (By.CSS_SELECTOR, "#riot-app > div > amount-inputs > div > div.amount > input")
    PROCEED = (By.CLASS_NAME, "submit")
    BONUS_ACTIVE = (By.CSS_SELECTOR, "label:nth-child(2)")
    TOTAL_AMOUNT = (By.CSS_SELECTOR, ".you-get > .value")
    YOU_GET = (By.CSS_SELECTOR, "#riot-app > div > total > div > div.you-get > div.value")


class FinalPageLocators:
    PHONE = (By.CSS_SELECTOR, "phone > div > div > div.form > div > div.right > input")
    PHONE_PROCEED = (By.CSS_SELECTOR, "#riot-app > div > phone > div > div > div.form > submit > div > a > span")
    PROCESSING_TEXT = (By.CSS_SELECTOR, "h1")
    BACK_LINK = (By.CSS_SELECTOR, "#riot-app > div > div.back > a")


class LoginPageLocators:
    LANGUAGE_BUTTONS = (By.CLASS_NAME, "languages-buttons")
    ENGLISH = (By.CSS_SELECTOR, "div.lang.en")
    RUSSIAN = (By.CSS_SELECTOR, "div.lang.ru")
    CHINESE = (By.CSS_SELECTOR, "div.lang.zh")
    KOREAN = (By.CSS_SELECTOR, "div.lang.ko")
    HINDI = (By.CSS_SELECTOR, "div.lang.hi")
    LOGIN_FORM = (By.CLASS_NAME, "login-form")
    USER_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "login-form > form > div.submit.gold")
    FORGOT_PASSWORD_LINK = (By.CLASS_NAME, "forgot")
    PASSWORD_RESTORE_INPUT = (By.NAME, "forgotPass")
    PASSWORD_RESTORE_BUTTON = (By.CSS_SELECTOR, "forgot-password > form > button")
    PASSWORD_RESTORE_NOTE = (By.CSS_SELECTOR, "forgot-password > form > button")
    PASSWORD_RESTORE_TEXT = (By.CLASS_NAME, "text")
    PASSWORD_CLOSE_NOTIFICATION = (By.CLASS_NAME, "close")
    WRONG_PASS = (By.CLASS_NAME, "notification")
    WRONG_PASS_TEXT = (By.CSS_SELECTOR, "login-form > notifications > div > div > div.text")
    CLOSE_WRONG_PASS = (By.CLASS_NAME, "close")
