from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_NAME_PRODUCT = (By.CSS_SELECTOR, "div .alert:nth-child(1) strong")
    ADDED_PRICE_PRODUCT = (By.CSS_SELECTOR, "div .alert:nth-child(3) strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div .product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div .product_main p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(2)")


