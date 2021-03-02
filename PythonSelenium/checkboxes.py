from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute('value') == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radiobuttons = driver.find_elements_by_css_selector("[class='radioButton']")
radiobuttons[1].click()
assert radiobuttons[1].is_selected()

#driver.close()
