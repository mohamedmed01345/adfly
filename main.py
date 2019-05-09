#!/usr/bin/env python 
from selenium import webdriver
from time import sleep
import random as rnd
print(r""" CODED BY :
 ___  _ _  _ _  ___  _  ___
| . || \ || | || . >| |/ __>
|   ||   || ' || . \| |\__ \
|_|_||_\_|`___'|___/|_|<___/

Contact : https://github.com/mohamedmed01345
          +201200840441
          https://www.facebook.com/Anubis-549848145502585
""".center(20,"="))
blg_link = input("Enter your Blogger Link : ")
adf_link = input("Enter your Ad.fly Link : ")
proxy = open("proxy.txt","r")
prxa = proxy.readlines()
rnd.shuffle(prxa)
def srata() :
    prxaa = sample(prxa,1)
    myProxy = prxaa[0].strip()
    webdriver.DesiredCapabilities.FIREFOX["proxy"] = {
    "httpProxy":myProxy,
    "ftpProxy":myProxy,
    "sslProxy":myProxy,
    #"noProxy":None,
    "proxyType":"MANUAL"
    #"autodetect":True
    }
    firefox = webdriver.FirefoxOptions()
    firefox.add_argument("--private")
    driver = webdriver.Firefox(options = firefox)
    driver.get(blg_link)
    x = driver.find_element_by_link_text(adf_link)
    x.click()
    sleep(7)
    x1 = driver.find_element_by_xpath("/html/body/div[6]/table/tbody/tr[1]/td/div/div[1]/span[2]/a/img")
    x1.click()
    driver.close
for b in prxa :
    srata()
