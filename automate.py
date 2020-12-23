from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

def clickByXpath(str):
    driver.implicitly_wait(5)
    elem=driver.find_element_by_xpath(str)
    elem.click() 
    
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://tinder.com')
#reject cookies
clickByXpath('/html/body/div[1]/div/div[2]/div/div/div[2]/button')
driver.implicitly_wait(5)
clickByXpath('/html/body/div[2]/div/div/div/div[3]/div[2]/button')
driver.implicitly_wait(2)
#login button
clickByXpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')

#more option 1
try:
    clickByXpath('//button[contains(text(), "More Options")]')
except (StaleElementReferenceException,NoSuchElementException) as e:
    pass

driver.implicitly_wait(3)

try:
    clickByXpath('//button[contains(text(), "More Options")]')
except (StaleElementReferenceException,NoSuchElementException) as e:
    pass
#login by phone num


#clickByXpath('//button[contains(text(), "Log in with phone number")]')
clickByXpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[3]/button/span[2]')

#enter phone num
elem=driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
elem.send_keys("8971365047")
elem.send_keys(Keys.RETURN)
driver.implicitly_wait(30)
#continue after phone OTP
clickByXpath('//*[@id="modal-manager"]/div/div/div[1]/button')
driver.implicitly_wait(30)
#confirm email
clickByXpath('//*[@id="modal-manager"]/div/div/div[1]/button')
elem.send_keys(Keys.RETURN)
time.sleep(35)


try:
    clickByXpath('//button[contains(text(), "Allow")]')
except (StaleElementReferenceException,NoSuchElementException) as e:
    pass



driver.implicitly_wait(5)
elem.send_keys(Keys.TAB)
elem.send_keys(Keys.TAB)
elem.send_keys(Keys.RETURN)
driver.implicitly_wait(5)
clickByXpath('//button[contains(text(), "Enable")]')

try:
    clickByXpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
except NoSuchElementException:
    pass
driver.implicitly_wait(3)


