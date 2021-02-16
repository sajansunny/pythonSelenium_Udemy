from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("Sajan")
driver.find_element_by_css_selector("input[name='name']").send_keys("Sajan")
driver.find_element_by_name("email").send_keys("sajan.sunny@outlook.com")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)
