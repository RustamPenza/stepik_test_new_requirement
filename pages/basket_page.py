from .locators import BasketPageLocators
from .locators import BasePageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Basket is not empty message, but should be"

    def should_be_success_message(self):
        assert self.is_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
            "No success message, but it should be"

    def should_cant_see_basket_link(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_LINK), \
            "Can see basket link, but should not be"
