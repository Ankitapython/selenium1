from selenium import webdriver

p=webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')
p.find_element_by_name('username')
p.find_element_by_name('password')
p.find_element_by_name('login').click()
