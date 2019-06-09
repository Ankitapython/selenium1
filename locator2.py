from selenium import webdriver

p=webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe")
p.get("https://www.naukri.com/account/register/basicdetails")
p.find_element_by_id("fname").send_keys("riya")
p.find_element_by_name("email").send_keys("riya@gmail.com")
p.find_element_by_xpath("//input[@placeholder='Minimum 6 characters']").send_keys("riya77")
p.find_element_by_xpath("//input[@name='number']").send_keys("9876543901")
p.find_element_by_name("city").send_keys("Belgaum")
p.find_element_by_name("uploadCV").send_keys("cv.pdf")
p.find_element_by_name("basicDetailSubmit").click()
