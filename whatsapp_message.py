from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import os,time
path = "user-data-dir=C:\\Users\\**Insert your name here (Laptop user name)**\\AppData\\Local\\Microsoft\\Edge\\User Data\\Whatsapp"    #path to save user data
ext = webdriver.EdgeOptions()
ext.add_argument(path)
driver = webdriver.Edge(options=ext)
wait = WebDriverWait(driver,10**4)
file = open("data.txt","r")         #reading phone numbers from a .txt file 
wait1 = WebDriverWait(driver,1)
phones = file.readlines()
no_whatsapp = list()
for i in range(len(phones)):
    ph = phones[i]
    website = "https://web.whatsapp.com/send?phone=%2B91" + ph + "&text&app_absent=0"
    driver.get(website)
    res = False
    while res is False:
        try:
            wait1.until(ec.element_to_be_clickable((By.XPATH,'//div[@title="Type a message"]'))).send_keys("Test message")
            wait1.until(ec.element_to_be_clickable((By.XPATH, '//div[@title="Type a message"]'))).send_keys(Keys.ENTER)
            time.sleep(1)
            res = True
        except:
            try:
                wait1.until(ec.element_to_be_clickable((By.XPATH,'//div[contains(text(),"Phone number shared via url is invalid.")]')))
                no_whatsapp.append(ph.strip())
                res = True
            except:
                pass
if len(no_whatsapp) > 0:
    print("The numbers which are incorrect or without whatsapp account are:")
    print(no_whatsapp)
