import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()


chrome_driver = os.getenv("CHROME_DRIVER")
ser = Service(chrome_driver)
driver = webdriver.Chrome(service=ser)

URL = "https://www.trademe.co.nz/a/property/residential/rent/auckland/north-shore-city/northcross/search?bedrooms_min=3&bathrooms_min=1&available_now=true"
GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfQiVWDSa1vTmo1DTTfaDKJFKDLam74Emu8Rq-RcCBVfSq4Ag/viewform?usp=sf_link"

driver.get(URL)

#Create a list of addresses
addresses = driver.find_elements(By.CSS_SELECTOR, 'tm-property-search-card-listing-title')
all_addresses = []
for address in addresses:
    all_addresses.append(address.text)


#Create a list of prices
prices = driver.find_elements(By.CSS_SELECTOR, ".tm-property-search-card-price-attribute__price")
all_prices = []
for price in prices:
    all_prices.append(price.text)


#Create a list of links for listings
links = driver.find_elements(By.CSS_SELECTOR, '.tm-progressive-image-loader__full')
all_links = []
for link in links:
    all_links.append(link.get_attribute("src"))


# #Fill out the form
time.sleep(2)
for n in range(len(all_addresses)):
    driver.get(GOOGLE_FORM)
    time.sleep(2)

    address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address_field.send_keys(all_addresses[n])
    price_field.send_keys(all_prices[n])
    link_field.send_keys(all_links[n])
    submit_button.click()







