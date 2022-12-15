from pages.global_variables import MONEY_US


def currency_converter(currency, bonus=False):
    if bonus is True:
        bonus_value = 2
    else:
        bonus_value = 1
    if currency == "ru":
        rate = 50000 / 1000 * bonus_value
    elif currency == "cnh":
        rate = 6888 / 1000 * bonus_value
    else:
        rate = 1 * bonus_value
    return {nm: wm * rate for (nm, wm) in zip(MONEY_US.keys(), MONEY_US.values())}
