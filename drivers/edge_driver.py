from selenium import webdriver
from selenium.webdriver.edge.options import Options

class EdgeDriver:
    def create_driver(self):
        options = Options()
        options.use_chromium = True
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('--disable-gpu')
        options.add_argument('start-maximized')
        return webdriver.Edge(options=options)