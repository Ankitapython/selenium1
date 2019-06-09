from selenium import webdriver
from selenium.webdriver.common.keys import Keys
d = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')
d.get('https://www.google.com')
d.find_element_by_name('q').send_keys('kissasian')
d.find_element_by_name('q').send_keys(Keys.ENTER)
#d.find_element_by_name('btnK')