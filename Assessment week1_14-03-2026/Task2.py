from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org/")
sleep(2)

search_box = driver.find_element(By.ID, "searchInput")
print("Search box found:", search_box)

english = driver.find_element(By.ID, "js-link-box-en")
print("English language found:", english.text)


logo = driver.find_element(By.CLASS_NAME, "central-featured-logo")
print("Logo found:", logo)


languages = driver.find_elements(By.CSS_SELECTOR, ".central-featured-lang")
print("Total language links in central block:", len(languages))

sleep(2)


driver.back()
sleep(2)


driver.forward()
sleep(2)

driver.refresh()
sleep(2)

print("Final Page Title:", driver.title)

driver.quit()