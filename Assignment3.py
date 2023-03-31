from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.youtube.com/")
time.sleep(3)

# Finding the search bar and entering text
search_bar = driver.find_element("name", "search_query")
search_bar.send_keys("baby shark song")

search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

assert "baby shark song - YouTube" in driver.title

# Finding the element to play the song
element = driver.find_element(By.LINK_TEXT, "Baby Shark Dance | #babyshark Most Viewed Video | Animal Songs | PINKFONG Songs for Children")
element.click()
time.sleep(5)

# Finding the element to redirect to home page
home = driver.find_element(By.ID, "logo")
home.click()

assert "YouTube" in driver.title
time.sleep(5)

# Finding the element to clear the search box
clear_search = driver.find_element(By.CSS_SELECTOR, "#search-clear-button .yt-spec-touch-feedback-shape__fill")
clear_search.click()

time.sleep(5)

# Closing the webdriver
driver.close()


