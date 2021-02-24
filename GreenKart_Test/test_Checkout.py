import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

items = []
cart_items = []
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
add_buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for add_button in add_buttons:
    items.append(add_button.find_element_by_xpath("parent::div/parent::div/h4").text)
    add_button.click()

print(items)

driver.find_element_by_xpath("//a[@class='cart-icon']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

web_cart_items = driver.find_elements_by_css_selector("p.product-name")
for web_cart_item in web_cart_items:
    cart_items.append(web_cart_item.text)
print(cart_items)
assert items == cart_items


#item_total_rows = driver.find_elements_by_xpath("//table[@class='cartTable']/tbody/tr/td[5]")
item_total_rows = driver.find_elements_by_xpath("//tr/td[5]/p")

item_total = 0.0
for item_total_row in item_total_rows:
    item_total = (item_total + int(item_total_row.text))
print(item_total)

total_amt = float(driver.find_element_by_xpath("//span[@class='totAmt']").text)
print(total_amt)
assert item_total == total_amt

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element_by_css_selector(".promoInfo").text)
total_aft_dis = float(driver.find_element_by_xpath("//span[@class='discountAmt']").text)
discount_per_act = driver.find_element_by_xpath("//span[@class='discountPerc']").text
print(discount_per_act[0:2])

discount_per = int(((total_amt - total_aft_dis)/total_amt)*100)
print(discount_per)

assert discount_per == int(discount_per_act[0:2])
driver.close()

