from selenium import webdriver

try:
    browser = webdriver.Chrome(
        executable_path='C:/chromedriver.exe')  # путь до драйвера
    browser.get("http://shop.bugred.ru/user/login/index")

    input1 = browser.find_element_by_id("exampleInputEmail1")
    input1.send_keys('test@mail.com')
    input2 = browser.find_element_by_id("exampleInputPassword1")
    input2.send_keys('1')
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
    text = browser.find_element_by_id("navbarDropdown2").text
    assert "Test" in text

finally:
    browser.quit()
