from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket(self, name, price):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), ("Button 'Add to basket' "
                                                                                 "is not presented")
        button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()
        self.should_be_name_product(name)
        self.should_be_price_product(price)

    def should_be_name_product(self, name):
        add_name = self.browser.find_element(*ProductPageLocators.ADDED_NAME_PRODUCT).text
        assert name == add_name, f"Wait '{name}', have '{add_name}'"

    def should_be_price_product(self, price):
        add_price = self.browser.find_element(*ProductPageLocators.ADDED_PRICE_PRODUCT).text
        assert price == add_price, f"Wait '{price}', have '{add_price}'"
