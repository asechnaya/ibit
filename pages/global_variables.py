import configparser

COW_GROUP = "15"
PREFIX = "https://"
LINK = "ibitcy.com/interview/qa/mobile-deposit/"
PAY_LINK = "ibitcy.com/interview/qa/mobile-deposit/#/payment"
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8-sig')
USER, PASSWORD = config.get("DEMO", 'Email'), config.get("DEMO", "Password")
AUTH_LINK = PREFIX + USER + ":" + PASSWORD + "@" + LINK

OK_TEXT_EN = "Новый пароль успешно отправлен на Вашу почту"
OK_TEXT_RU = "New password was sent to your email address"
OK_TEXT_KO = "새 암호가 성공적으로 전자 메일로 보내졌다"
OK_TEXT_CH = "新密碼已發送至您的電子郵箱"
OK_TEXT_HI = "आपके ईमेल पते पर नया पासवर्ड भेजा गया था"

OK_TEXT = {"ru": OK_TEXT_RU,
           "en": OK_TEXT_EN,
           "ko": OK_TEXT_KO,
           "ch": OK_TEXT_CH,
           "hi": OK_TEXT_HI}

NOT_OK_TEXT = "No such email address"
PROCESSING_TEXT_RU = "ВАША ЗАЯВКА ОБРАБАТЫВАЕТСЯ, ПОЖАЛУЙСТА ПОДОЖДИТЕ"
PROCESSING_TEXT_EN = "YOUR PAYMENT IS BEING PROCESSED"
PROCESSING_TEXT_HI = "आपका भुगतान प्रोसेस किया जा रहा है"
PROCESSING_TEXT_KO = "Some korean text"
PROCESSING_TEXT_CH = "Some chinese text"

FINAL_TEXT = {"ru": PROCESSING_TEXT_RU,
              "en": PROCESSING_TEXT_EN,
              "ko": PROCESSING_TEXT_KO,
              "ch": PROCESSING_TEXT_CH,
              "hi": PROCESSING_TEXT_HI}

BAR_LOCATOR = {"vip": "width: 80%;",
               "gold": "width: 60%;",
               "silver": "width: 40%;",
               "mini": "width: 20%;"}

BAR_COLOR = {"vip": "rgba(153, 85, 232, 1)",
             "gold": "rgba(226, 199, 81, 1)",
             "silver": "rgba(197, 200, 201, 1)",
             "mini": "rgba(64, 174, 249, 1)"}

MONEY_US = {"vip": 2500,
            "gold": 1000,
            "silver": 500,
            "mini": 200}

PAYSYS = {1: 'VISA, MasterCard, Maestro',
          2: 'VISA, MasterCard, Visa Electron',
          3: 'VISA, MasterCard, Maestro',
          4: 'VISA, MasterCard (2)',
          5: 'Skrill',
          6: 'Neteller',
          7: 'Perfect Money',
          8: 'Fasapay',
          9: 'Payweb',
          10: 'WebMoney',
          11: 'UnionPay',
          12: 'UnionPay 2',
          13: 'QIWI',
          14: 'Яндекс.Деньги'}
