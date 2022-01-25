import random,time,os
from tkinter import X
cwd = os.getcwd()
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import json

from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
 
mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 650, "pixelRatio": 3.4 },
    }

firefox_options = webdriver.ChromeOptions()
firefox_options.add_argument('--no-sandbox')
 
firefox_options.headless = False
firefox_options.add_argument('--disable-setuid-sandbox')
firefox_options.add_argument('disable-infobars')
firefox_options.add_argument('--ignore-certifcate-errors')
firefox_options.add_argument('--ignore-certifcate-errors-spki-list')

firefox_options.add_argument("--incognito")
firefox_options.add_argument('--no-first-run')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument("--disable-infobars")
firefox_options.add_argument("--disable-extensions")
firefox_options.add_argument("--disable-popup-blocking")
firefox_options.add_argument('--log-level=3') 
firefox_options.add_argument("--window-size=500,1600")
firefox_options.add_argument('--disable-blink-features=AutomationControlled')
firefox_options.add_experimental_option("useAutomationExtension", False)
firefox_options.add_experimental_option("excludeSwitches",["enable-automation"])
firefox_options.add_experimental_option('excludeSwitches', ['enable-logging'])
firefox_options.add_argument('--disable-notifications')

from faker import Faker
fake = Faker('en_US')
from selenium.webdriver.common.action_chains import ActionChains
random_angka = random.randint(100,999)
random_angka_dua = random.randint(10,99)
def xpath_ex(el):
    element_all = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all)

def xpath_long(el):
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all) 

def xpath_type(el,word):
    return wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el))).send_keys(word)
def xpath_id(el,word):
    return wait(browser,30).until(EC.presence_of_element_located((By.XPATH, f'//input[@{el}]'))).send_keys(word)
def login(datas):
    data = datas.split("|")
    email = data[0]
    no_hp = data[1]
    global browser
     
   
    firefox_options.add_experimental_option("mobileEmulation", mobile_emulation)
 
    firefox_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")
    browser = webdriver.Chrome(options=firefox_options,executable_path=f"{cwd}\\chromedriver.exe")
    browser.get('https://www.unipin.com/id/game/unipin-voucher-id')
    get_price = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, f'(//button[contains(text(),"{price}")])[1]'))).get_attribute("data-id")
    browser.get(f'https://www.unipin.com/game/checkout/1402/56/{get_price}?ifc=undefined')
    xpath_type('//input[@type="email"]',email)
    xpath_type('//input[@type="tel"]', no_hp)
   
    xpath_ex('//input[@id="payment-checkout-button"]')
    print(f"[*] Next!")
    
if __name__ == '__main__':
    print("[*] Unipin Check Out")
    global price
    price = input('[*] Input Harga: ')
     
    myfile = open(f"{cwd}\\list.txt","r")
    list_account = myfile.read()
    list_accountsplit = list_account.split("\n")
    for i in list_accountsplit:
        login(i)
    