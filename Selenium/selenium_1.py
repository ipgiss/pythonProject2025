# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# options = webdriver.ChromeOptions()
#
# options.add_experimental_option('detach', True)
# options.add_argument("--no-sandbox")
#
# s = Service('C:\\Users\\kuzne\\git\\pythonProject2025\\chromedriver.exe')
#
# driver = webdriver.Chrome(service=s, options=options)

## вар.2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
