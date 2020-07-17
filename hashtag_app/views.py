from django.shortcuts import render
import requests
from django.http import HttpResponse
import random
import json 
from django.views.generic import View
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from time import sleep

import runme

class generator(View):
    
    def post(self, *args, **kwargs):
        keyword = self.request.POST['keyword']
        if '#' in keyword:
            pass
        else:
            keyword = '#'+keyword
        drivers = runme.drivers
        d = drivers[0]

        ctextarea = WebDriverWait(d, 20).until(EC.element_to_be_clickable((By.XPATH, 
        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
        ctextarea = d.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        ctextarea.clear()
        ActionChains(d).move_to_element(ctextarea).click(ctextarea).send_keys(keyword).perform()

        sleep(1)
        fetched_hashtags = []
        for elem in d.find_elements_by_xpath('.//span'):
            fetched_hashtags.append(elem.get_attribute("innerHTML"))
        hashtags = []
        for i in fetched_hashtags:
            if i == '':
                pass
            elif keyword in i:
                hashtags.append(i+' ')
            else:
                pass
        return HttpResponse(hashtags)
