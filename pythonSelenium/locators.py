from selenium import webdriver
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("Sajan")
driver.find_element_by_css_selector("input[name='name']").send_keys("Sajan")
driver.find_element_by_name("email").send_keys("sajan.sunny@outlook.com")
driver.find_element_by_id("exampleCheck1").click()
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
driver.find_element_by_xpath("//input[@type='submit']").click()
#print(driver.find_element_by_class_name("alert-success").text)
message = driver.find_element_by_class_name("alert-success").text
assert "success" in message
driver.close()
