from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
driver.get('https://google.com')
elem=driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)