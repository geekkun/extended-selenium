# -*- coding: utf-8 -*-
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from random import randint
import rstr
import time
import pickle
import sys
import os
# reload(sys)
# sys.setdefaultencoding('utf8')

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('disable-gpu')
# options.add_argument('remote-debugging-port=9000')

browser = webdriver.Chrome(chrome_options=options)

# browser = webdriver.Chrome()


# with_count hearted

# browser = webdriver.PhantomtextS(service_args=["--remote-debugger-port=9000"])
# browser.set_window_size(1120, 550)

def get(element):
    browser.get(element)

def css(element, prop):
    browser.find_element_by_xpath(element).value_of_css_property(prop)

def stopWatch(value):
    '''From seconds to Days;Hours:Minutes;Seconds'''

    valueD = (((value/365)/24)/60)
    Days = int (valueD)

    valueH = (valueD-Days)*365
    Hours = int(valueH)

    valueM = (valueH - Hours)*24
    Minutes = int(valueM)

    valueS = (valueM - Minutes)*60
    Seconds = int(valueS)

    valueMS = (valueS - Seconds)*1000
    MSec = int(valueMS)

    print (Seconds,":",MSec)
    return Seconds


# ADD REDO FOR INCORRECT POSTCODE - low priority
def postcode(element):
    posty = element
    pattern = re.compile(postcode_reg)
    pattern.match(posty)
    return posty.upper()

def wait(element):
    time.sleep(element)

def postcode_gen(element):
    postcoded = element
    a = randint(0,9)
    rs = rstr.xeger('[abd-htextlnp-uw-zABD-HtextLNP-UW-Z]')
    r = rstr.xeger('[abd-htextlnp-uw-zABD-HtextLNP-UW-Z]')
    postcoded += " "+str(a)+rs+r
    return postcoded

def waiter_xpath(element, time=10):
    try:
        WebDriverWait(browser, time).until(
            EC.presence_of_element_located((By.XPATH, element))
        )
    except:
        waitr(element)


def waiterID(element, time=10):
    WebDriverWait(browser, time).until(
        EC.presence_of_element_located((By.ID, element))
    )

def waitr(element):
    WebDriverWait(browser, 17).until(
        EC.presence_of_element_located((By.XPATH, element))
    )

def click(element):
    waiter_xpath(element)
    browser.find_element_by_xpath(element).click()

def type(element, text):
    waiter_xpath(element)
    browser.find_element_by_xpath(element).send_keys(text + Keys.RETURN)

def clickID(element):
    waiter_xpath(element)
    browser.find_element_by_id(element).click()

def typeID(element, text):
    waiter_xpath(element)
    browser.find_element_by_id(element).send_keys(text + Keys.RETURN)


def typek(element, text):
    waiter_xpath(element)
    browser.find_element_by_xpath(element).send_keys(text)

def select(element, text):
    click(element)
    mySelect = Select(browser.find_element_by_xpath(element))
    mySelect.select_by_visible_text(text)


def pics(pat, type, max):
    # click(".//*[@id='post-ad-container']/div[6]/div/div/div[1]/ul/li/a") # not needed
    path = pat + type + str(randint(1, max)) + ".jpg"
    browser.find_element_by_css_selector("input[type=\"file\"]").send_keys(path)
