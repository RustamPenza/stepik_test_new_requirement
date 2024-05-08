from .locators import BasketPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_cant_see_product_in_basket_opened_from_main_page(self):
        self.go_to_basket_page()
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Product in basket, but should not be"
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Basket is no empy, but should be empty"
