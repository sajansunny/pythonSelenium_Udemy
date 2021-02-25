from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
mouse_hover = driver.find_element_by_id("mousehover")
action.move_to_element(mouse_hover).perform()
top = driver.find_element_by_link_text("Reload")
action.move_to_element(top).click().perform()
