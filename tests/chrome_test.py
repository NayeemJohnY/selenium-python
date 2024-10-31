from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get('http://selenium.dev/')
print('Title', driver.title)
