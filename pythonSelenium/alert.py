from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = "Sajan"
driver.find_element_by_css_selector("#name").send_keys(name)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
assert name in alert.text
alert.accept()

driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()

