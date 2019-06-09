from selenium import webdriver

sp=webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe")
sp.get("https://www.gmail.com")
sp.find_element_by_name('identifier').send_keys('ankiitamore')