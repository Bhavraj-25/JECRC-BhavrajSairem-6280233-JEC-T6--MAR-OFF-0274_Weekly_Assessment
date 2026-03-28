from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.vogue.in/")

driver.find_element(By.XPATH, "//a[text()='Shopping']").click()

sleep(2)

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Image may contain Accessories Adult Person and Headband']")))

sleep(2)

olive_crest = driver.find_element(By.XPATH, "//img[@alt='Image may contain Accessories Adult Person and Headband']")
driver.execute_script('arguments[0].scrollIntoView();', olive_crest)

sleep(2)

driver.find_element(By.XPATH, "//div[@id='69845cc157840edfb23334e7']").click()

sleep(2)

all = driver.window_handles
driver.switch_to.window(all[-1])

## Different method
# driver.switch_to.new_window('window')
# driver.get("https://heirra.com/collections/wings/products/olive-crest-wings?cid=65c3630e1ffe6b6f9d572b81")

sleep(2)
driver.implicitly_wait(5)

name=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='d-flex justify-content-between align-items-center pt-3 pb-2']/h1")))
print(name.text)
price=wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='product-price-final product-price-final-sale']/span[2]")))
print(price.text)

# name = driver.find_element(By.XPATH, "//h1[@class='product-title title mb-0 h2']")
# print(name.text)
# price = driver.find_element(By.XPATH, "(//span[@class='money buckscc-money'])[1]")
# print(price.text)