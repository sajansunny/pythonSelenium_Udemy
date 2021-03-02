from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
#driver = webdriver.Ie(executable_path="C:\\Drivers\\IEDriverServer.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.udemy.com/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
