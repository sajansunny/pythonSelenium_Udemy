from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("#username").send_keys("Sajan")
driver.find_element_by_css_selector(".password").send_keys("Sunny")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//a[text()='Cancel']").click()
