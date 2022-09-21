from page_objects.Admin_Page import Admin_Page


class Test_admin:
    def test_login_to_admin_page(self, browser):
        admin_page = Admin_Page(browser)
        admin_page.open_page()
        assert browser.title == "Administration"
        admin_page.login()
        assert browser.tittle == "Dashboard"

    def test_add_new_product_in_admin(self, browser):
        admin_page = Admin_Page(browser)
        admin_page.open_page()
        admin_page.login()
        product_name = "Test"
        admin_page.open_products_list()
        assert product_name not in admin_page.get_products_list(), f"Продукт {product_name} уже добавлен"
        admin_page.add_new_product(product_name)
        assert product_name in admin_page.get_products_list(), f"Продукт {product_name} ненайден"

    def test_delite_product_in_admin(self, browser):
        admin_page = Admin_Page(browser)
        admin_page.open_page()
        admin_page.login()
        product_name = "Test"
        admin_page.open_products_list()
        assert product_name in admin_page.get_products_list(), f"Продукт {product_name} ненайден"
        admin_page.delete_product()
        assert product_name not in admin_page.get_products_list(), f"Продукт {product_name} не удален"
