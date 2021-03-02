from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Sajan")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shop_button = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shop_button)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#driver.close()
