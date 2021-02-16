from selenium import webdriver

try:
    browser = webdriver.Chrome(
        executable_path='C:/chromedriver.exe')  # путь до драйвера
    browser.get("http://shop.bugred.ru")

    browser.execute_script("window.scrollBy(0,470);")
    picture1 = browser.find_element_by_xpath('//p[text()=\"dress_33"]')  # находим красное платье
    picture1.click()
    input1 = browser.find_element_by_id("exampleCount")
    input1.send_keys("1")  # вводим количество "1"
    button1 = browser.find_element_by_class_name("btn.btn-primary")  # "добавить в корзину"
    button1.click()
    button2 = browser.find_element_by_xpath('//a[text()=\"Все товары"]')
    button2.click()
    browser.find_elements_by_css_selector('a.page-link')[1].click()  # находим шорты с надписью
    picture2 = browser.find_element_by_xpath('//p[text()=\"Платье огонь 2"]')
    picture2.click()
    input2 = browser.find_element_by_id("exampleCount")
    input2.send_keys("1")  # вводим количество "1"
    button2 = browser.find_element_by_class_name("img.img.img-thumbnail")  # добавляем в корзину
    button2.click()
    button3 = browser.find_element_by_class_name("fas.fa-shopping-cart")  # заходим в корзину
    button3.click()
    button4 = browser.find_element_by_class_name("fas.fa-trash-alt")  # удаляем товар
    button4.click()

finally:
    browser.quit()
