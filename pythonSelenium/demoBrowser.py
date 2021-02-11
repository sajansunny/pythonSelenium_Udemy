from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)
driver.close()