from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action.double_click(driver.find_element_by_id("double-click")).perform()
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
