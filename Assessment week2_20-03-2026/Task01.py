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
driver.get("https:/www.amazon.com")

assert 'Amazon.com' in driver.title,'title not present'
assert 'https://www.amazon.com' in driver.current_url,'current_url not present'

sleep(2)

xpath_search = "//select[@class='nav-search-dropdown searchSelect nav-progressive-attrubute nav-progressive-search-dropdown']"
drop = driver.find_element(By.XPATH, xpath_search)
sel = Select(drop)
sel.select_by_visible_text("Books")

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("Harry Potter", Keys.ENTER)

wait = WebDriverWait(driver, 5)
load_wait = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='s-no-outline']//h2[text()='Results']")))

prod_titles = driver.find_element(By.XPATH, "//div[@data-cy='title-recipe'][1]/descendant::a[3]//span[1]")
print(prod_titles.title)

sleep(2)
driver.quit()