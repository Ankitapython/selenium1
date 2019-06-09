from selenium import webdriver
from selenium.webdriver.support.select import Select

dr=webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe")
dr.get("https://facebook.com")

dr.implicitly_wait(30)
dr.find_element_by_name("firstname").send_keys("Riya")
dr.find_element_by_xpath("//input[contains(@name,'lastname')]").send_keys("shetty")
dr.find_element_by_name("reg_email__").send_keys("8796541236")

day=dr.find_element_by_id("day")
s1=Select(day)
s1.select_by_index(2)

month=dr.find_element_by_id("month")
s2=Select(month)
s2.select_by_visible_text("Feb")

year=dr.find_element_by_id("year")
s3=Select(year)
s3.select_by_value("2016")