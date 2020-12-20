import time
from selenium import webdriver

try:
 browser = webdriver.Chrome(
        executable_path='')  #путь до драйвера
 browser.get("http://shop.bugred.ru/user/register/index")

 input1 = browser.find_element_by_id("exampleInputName")
 input1.send_keys('test')
 input2 = browser.find_element_by_id("exampleInputEmail1")
 input2.send_keys('test@mail.com')
 input3 = browser.find_element_by_id("exampleInputPassword1")
 input3.send_keys('1')
 input4 = browser.find_element_by_id("exampleInputPassword2")
 input4.send_keys('1')
 button = browser.find_element_by_class_name("btn.btn-primary")
 button.click()

finally:
    time.sleep(15)
    browser.quit()