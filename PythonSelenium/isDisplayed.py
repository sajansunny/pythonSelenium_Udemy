from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()
driver.close()