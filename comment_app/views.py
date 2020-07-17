from selenium.webdriver.support.ui import WebDriverWait
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse, redirect
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
import requests
from django.views.generic import View
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui

import runme


class comments(View):
    

    def post(self, *args, **kwargs):
        take_this_username = self.request.POST['take_this_username']
        url = self.request.POST['url_1']
        commented_txt = self.request.POST['comment']
        self.take_this_username = take_this_username
        self.commented_txt = commented_txt
        self.url = url
        return self.give_driver_id()

    def give_driver_id(self):
        self.drivers = runme.drivers
        uname_block = runme.uname_block
        indexofid = 0
        for ids in uname_block:
            if self.take_this_username == ids:
                indexofid = uname_block.index(self.take_this_username)
        self.indexofid = indexofid
        return self.commentit()

    def commentit(self):
        driver = self.drivers[self.indexofid]
        driver.get(self.url)
        sleep(1)
        comment = ''
        if self.commented_txt is None:
            comments = ['Cool Man', 'Awesome', 'Great']
            comment = comments[randint(0, 1)]
        else:
            comment = self.commented_txt
        try:
            ctextarea = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')))
            ctextarea = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
            ActionChains(driver).move_to_element(ctextarea).click(ctextarea).send_keys(comment).send_keys(Keys.ENTER).perform()
        except TimeoutError:
            print("timeout")
        return HttpResponse("Your Post Just Got Commented")
