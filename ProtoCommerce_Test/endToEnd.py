from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/shop")

product_names = driver.find_elements_by_xpath("//h4[@class='card-title']")
for product_name in product_names:
    if product_name.text == "Blackberry":
        product_name.find_element_by_xpath("parent::div/parent::div/div[2]/button").click()
        break
driver.find_element_by_xpath("//a[@class = 'nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_xpath("//input[@id='country']").send_keys("India")

checkbox = driver.find_element_by_xpath("//input[@id='checkbox2']")
driver.execute_script("arguments[0].click();", checkbox)
driver.find_element_by_xpath("//input[@type='submit']").click()
