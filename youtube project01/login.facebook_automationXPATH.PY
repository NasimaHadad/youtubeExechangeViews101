from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium import *
import os
import time

email='tv.marketing2020@gmail.com'
password='ABDELKARIMNASIMA8284@07NA@R'
comment=["أكثر توجه فاعلية ومردودية في مجال التسويق الإلكتروني والتجارة الإلكترونية ؟؟ https://www.youtube.com/watch?v=6-RlZkMTWsY&list=PLnMsaTc7T4ZTFpHoV6HvI1hZ1lS4JsEew&index=3?0s"]

base_url = 'https://www.facebook.com/'

sleep(10)

 driver = webdriver.Firefox()
driver.get(base_url)


EmailURL = "//input[@id='email']"
PasswordURL = "//input[@id='pass']"
ButtonURL = "//label[@class='login_form_login_button uiButton uiButtonConfirm']//input"
postCode = "//*[@name='xhpc_message']"


UserElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EmailURL))
UserElement.send_keys(email)


sleep(5)

PasswordElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(PasswordURL))
PasswordElement.send_keys(password)


sleep(5)

ButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(ButtonURL))
ButtonElement.click()


sleep(18)

CommentElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(postCode))
CommentElement.send_keys(comment)

sleep(5)

# postbtn=driver.find_elements_by_tag_name('button')
# for btn in postbtn:
#     print(btn.text)
#     if btn.text=='Post':
#         btn.click()

#_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft
#button=driver.find_element_by_css_selector('._1mf7._4r1q._4jy0._4jy3._4jy1._51sy.selected._42ft')


post_it=driver.find_element_by_xpath("//*[@id='u_0_1a']/div/div[6]/div/ul/li[2]/button")
post_it.click()
print ("Posted...")




        


