from drivers.edge_driver import EdgeDriver
from pages.log_in_page import LogIn
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.check_out_page import CheckoutPage
def main():
    try:
        edge_driver = EdgeDriver()
        driver = edge_driver.create_driver()
        driver.get("https://www.saucedemo.com/")
        log_in_instance = LogIn(driver)
        log_in_instance.click_log_in()
        assert 'https://www.saucedemo.com/inventory.html' == driver.current_url,'No se inicio sesion correctamente'
        main_page = MainPage(driver)
        main_page.add_items_to_cart()
        cart_page = CartPage(driver)
        cart_page.go_to_cart()
        assert 'https://www.saucedemo.com/cart.html' == driver.current_url,'No se redirigio a la pagina del carrito'
        cart_page.go_to_checkout()
        assert 'https://www.saucedemo.com/checkout-step-one.html' == driver.current_url,'No se redirigio a la pagina de checkout'
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_form('Juan','Perez','12345')
        checkout_page.go_to_checkout_overview()
        assert 'https://www.saucedemo.com/checkout-step-two.html' == driver.current_url,'No se redirigio a la pagina de checkout overview'
        checkout_page.finish_checkout()
        assert 'https://www.saucedemo.com/checkout-complete.html' == driver.current_url,'No se redirigio a la pagina de checkout complete'
        assert 'Thank you for your order!' == checkout_page.get_checkout_complete_message(),'Mensaje de compra no encontrado'
        checkout_page.navigate_home()
        assert 'https://www.saucedemo.com/inventory.html' == driver.current_url,'No se redirigio a la pagina principal'
        main_page.go_to_menu_options()
        main_page.go_to_logout()
        assert 'https://www.saucedemo.com/' == driver.current_url,'No se redirigio a la pagina principal'
    except Exception as e:
        print(e)
        driver.save_screenshot('screenshots/error.png')
    finally:
        driver.quit()

if __name__ == '__main__':
    main()