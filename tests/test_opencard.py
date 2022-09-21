from page_objects.Catalog_Page import Catalog_Page
from page_objects.Main_Page import Main_Page
from page_objects.Register_Page import Register_Page


def test_main_page(browser):
    main_page = Main_Page(browser)
    main_page.open_page()
    assert main_page.count_heading_links() == 7
    logo = main_page.shop_logo()
    assert logo.get_attribute("title") == "Your Store"
    search_placeholder = main_page.search_placeholder()
    assert search_placeholder == "Search"


def test_switch_currency(browser):
    main_page = Main_Page(browser)
    main_page.open_page()
    main_page.change_currency("EUR")
    assert main_page.CURRENCY["EUR"] == main_page.current_sign_currency


def test_catalog_page(browser):
    catalog_page = Catalog_Page(browser)
    catalog_page.open_laptop_page()
    assert browser.title == "Laptops & Notebooks"
    assert catalog_page.count_product_cards == 5
    catalog_page.sort_products_by("Price (High > Low)")
    assert catalog_page.get_current_sort_filter == "Price (High > Low)"


def test_user_registration(browser):
    register_page = Register_Page(browser)
    register_page.open_page()
    register_page.create_new_user()
    assert "Your Account Has Been Created!" in register_page.success_register_message
