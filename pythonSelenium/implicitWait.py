import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
products = driver.find_elements_by_xpath("//div[@class='products']/div")
product_names = driver.find_elements_by_xpath("//h4[@class='product-name']")
add_buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for product_name in product_names:
    print(product_name.text)
    assert "ber" in product_name.text

for add_button in add_buttons:
    add_button.click()
assert len(add_buttons) == int(driver.find_element_by_xpath("//div[@class='cart-info']/table/tbody/tr/td/strong").text)

driver.find_element_by_xpath("//a[@class='cart-icon']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector(".promoInfo").text)

