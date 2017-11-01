from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#driver = webdriver.Firefox()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://finance.yahoo.com/quote/MMM/")
python_button = driver.find_elements_by_xpath("//*[@id='quote-nav']/ul/li[4]/a")
python_button.click()
