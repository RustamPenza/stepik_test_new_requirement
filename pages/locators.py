from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    INVALID_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link_inv")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn")


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


class BasketPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(2)")
    EMPTY_MESSAGE = (By.XPATH, "//p[contains(text(), 'Ваша корзина пуста')]")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner div.basket-title")


