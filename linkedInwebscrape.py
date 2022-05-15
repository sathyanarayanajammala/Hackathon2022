# -*- coding: utf-8 -*-
"""
Created on Sat May 14 11:18:35 2022

@author: jamal
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
  
# Creating an instance
driver = webdriver.Chrome("C:\Hackathon\chromedriver_win32\chromedriver")
  
# Logging into LinkedIn
driver.get("https://linkedin.com/uas/login")
time.sleep(5)
  
username = driver.find_element_by_id("username")
username.send_keys("sathyanarayana.jammala@gmail.com")  # Enter Your Email Address
  
pword = driver.find_element_by_id("password")
pword.send_keys("Krishn@9889")        # Enter Your Password
  
driver.find_element_by_xpath("//button[@type='submit']").click()

# Opening Kunal's Profile
# paste the URL of Kunal's profile here
profile_url = "https://www.linkedin.com/in/kunalshah1/"
  
driver.get(profile_url) 

start = time.time()
  
# will be used in the while loop
initialScroll = 0
finalScroll = 1000
  
while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})                          ")
    # this command scrolls the window starting from
    # the pixel value stored in the initialScroll 
    # variable to the pixel value stored at the
    # finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000
  
    # we will stop the script for 3 seconds so that 
    # the data can load
    time.sleep(3)
    # You can change it as per your needs and internet speed
  
    end = time.time()
  
    # We will scroll for 20 seconds.
    # You can change it as per your needs and internet speed
    if round(end - start) > 20:
        break
    
src = driver.page_source
  
# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')

# Extracting the HTML of the complete introduction box
# that contains the name, company name, and the location
intro = soup.find('div', {'class': 'pv-text-details__left-panel'})
  
print(intro)

name_loc = intro.find("h1")
  
# Extracting the Name
name = name_loc.get_text().strip()
# strip() is used to remove any extra blank spaces
print("Name:",name)
works_at_loc = intro.find("div", {'class': 'text-body-medium'})
  
# this gives us the HTML of the tag in which the Company Name is present
# Extracting the Company Name
works_at = works_at_loc.get_text().strip()
  
  
location_loc = intro.find_all("span", {'class': 'text-body-small'})
  
# Ectracting the Location
# The 2nd element in the location_loc variable has the location
#location = location_loc[1].get_text().strip()
  
print("Name -->", name,
      "\nWorks At -->", works_at,
      "\nLocation -->")