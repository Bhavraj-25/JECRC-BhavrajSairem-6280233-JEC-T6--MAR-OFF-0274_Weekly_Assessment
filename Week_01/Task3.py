from selenium import webdriver
from time import sleep

websites = [
    "https://www.thesouledstore.com",
    "https://www.nike.com",
    "https://www.bbc.com",
    "https://www.python.org"
]

driver = webdriver.Chrome()

for site in websites:
    sleep(3)
    driver.get(site)

    print("Website:", site)
    print("Title:", driver.title)
    print("-" * 40)

driver.quit()