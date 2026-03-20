from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.maximize_window()
driver.get("https://automationexercise.com/signup")

name = driver.find_element(By.XPATH, "//input[@data-qa='signup-name']")
name.send_keys("Bhavraj")
mail = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
mail.send_keys("sairem.bhavraj2512999999888888@gmail.com")

driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID, "id_gender1")))

driver.find_element(By.ID, "id_gender1").click()

news = driver.find_element(By.ID, "newsletter").click()
offer = driver.find_element(By.ID, "optin").click()
print(news.get_attribute("checked"))
print(offer.get_attribute("checked"))

sleep(2)
driver.quit()