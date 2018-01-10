# -*- coding: utf-8 -*-

import numpy as np
from time import sleep # So we don't request too much from the server
from selenium import webdriver
from selenium.webdriver.common import action_chains, keys # May not need?


'''
Initialize Chrome Driver

'''
def initialize_browser():

    my_options = webdriver.ChromeOptions()
    driver_path = "C:/Data/chromedriver.exe"
    my_options.add_argument("--disable-extensions")
    my_options.add_argument("--profile-directory=Default")
    my_options.add_argument("--incognito")
    my_options.add_argument("--disable-plugins-discovery")
    my_options.add_argument("--start-maximized")
    my_options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(executable_path = driver_path, chrome_options = my_options)

    return browser

'''
Baidu for English to Canto characters
Chineseconverter.com for Canto characters to Jyutping
'''

def to_jyutping(sentence):

    browser = initialize_browser()
    browser.get("http://fanyi.baidu.com/#en/yue")
    input_english = browser.find_element_by_id("baidu_translate_input")
    input_english.send_keys(sentence)
    sleep(3)# If I don't do sleep then it sometimes doesn't find the element
    # Unicode to deal with Chinese characters ? May not be needed?
    chinese_characters = browser.find_element_by_xpath('//*[@id="main-outer"]/div/div/div/div[2]/div[1]/div[2]/div/div/div[1]/p[2]').text
    browser.close
    browser = initialize_browser()
    browser.get("https://www.chineseconverter.com/cantonesetools/en/cantonese-to-jyutping")
    #sleep(1)
    input_characters = browser.find_element_by_id("text")
    #sleep(2)
    input_characters.send_keys(chinese_characters) # This gives the problem
    #sleep(2)
    convert_button = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div/div[2]/form/div[3]/div/button").click()
    jyutping = browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div/div[2]/form/div[1]/div[2]/div/div/div/div').text
    
    return jyutping, chinese_characters

def main():
    sentence = input('Enter your input: ')
    jyutping, chinese_characters = to_jyutping(sentence)
    #print("English: " + sentence)
    print("Traditional characters: " + chinese_characters)
    print("Cantonese Jyutping: " + jyutping)
    
if __name__ == '__main__':
    main()    