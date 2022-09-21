from selenium.webdriver.common.by import By

from Base_Page import Base_Page


class Main_Page(Base_Page):
    HEADER_LINKS = (By.CSS_SELECTOR, "#top-links li")
    LOGO = (By.CSS_SELECTOR, "#logo img")
    SEARCH_FIELD = (By.CSS_SELECTOR, "#search > input")
    CURRENCY = {
        "GBP": "£",
        "EUR": "€",
        "USD": "$"
    }
    CURRENCY_BTN = (By.CSS_SELECTOR, "#top .btn-group")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#top .btn-group .dropdown-menu")
    CURRENCY_SIGN = (By.CSS_SELECTOR, "button.btn-link strong")

    def count_heading_links(self):
        return len(self._verify_elements_presence(self.HEADER_LINKS))

    def shop_logo(self):
        return self._verify_element_visibility(self.LOGO)

    def search_placeholder(self):
        search = self._verify_element_visibility(self.SEARCH_FIELD)
        return search.get_attribute("placeholder")

    def change_currency(self, value):
        self._find_element_and_click(self.CURRENCY_BTN)
        self._verify_element_visibility(self.CURRENCY_DROPDOWN)
        self._find_element_and_click((By.CSS_SELECTOR, f".currency-select[name='{value}']"))

    @property
    def current_sign_currency(self):
        return self._verify_element_visibility(self.CURRENCY_SIGN).text
