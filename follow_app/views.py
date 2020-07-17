import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse, redirect
from selenium import webdriver
from time import sleep
from follow_app import models
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import requests
from django.views.generic import View
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import runme

class followers(View):

    def post(self, *args, **kwargs):
        username = self.request.POST['username']
        url = self.request.POST['url_1']
        u = ''
        try:
            u = models.used_by.objects.get(user=username)
        except ObjectDoesNotExist:
            u = models.used_by.objects.create(user=username)
            for i in models.insta_id.objects.all():
                models.left_id.objects.create(link=u, username=i.username)
        self.user = u
        self.username = username
        self.url = url
        return self.give_driver_id()

    def give_driver_id(self):
        uname_block = runme.uname_block
        try:
            c = models.left_id.objects.filter(link=self.user)
            d = (len(c) - 1)
            if d == -1:
                return HttpResponse("Outdated")
            elif d == 0:
                left_username = c[0].username
                print(left_username)
            else:
                r = randint(0, d)
                left_username = c[r].username
                print(left_username)
        except ValueError:
            return HttpResponse("Please Try Again...")
        indexofid = 0
        for ids in uname_block:
            if left_username == ids:
                indexofid = uname_block.index(left_username)
        self.left_username = left_username
        self.indexofid = indexofid
        return self.follow_him()

    def follow_him(self):
        self.drivers = runme.drivers
        driver = self.drivers[self.indexofid]
        driver.get(self.url)
        try:
            sleep(1)
            flw_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
            if flw_btn:
                flw_btn.click()
                print("Ipad_Mobile Followed")
        except (ElementClickInterceptedException, NoSuchElementException):
            try:
                flw_btn = driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
                if flw_btn:
                    ActionChains(driver).move_to_element(flw_btn).click(flw_btn).perform()
                    print("PCFollowed")
            except (ElementClickInterceptedException, NoSuchElementException):
                try:
                    flw_btn = driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/main/div/header/section/div[1]/button')
                    if flw_btn:
                        sleep(0.2)
                        ActionChains(driver).move_to_element(flw_btn).click(flw_btn).perform()
                        print("Private Account Followed")
                except (ElementClickInterceptedException, NoSuchElementException):
                    try:
                        unflw_btn = driver.find_element_by_xpath(
                            '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button')
                        if unflw_btn:
                            print("Account Already Followed")
                    except (ElementClickInterceptedException, NoSuchElementException):
                        return HttpResponse("Instagram Has Restrict Our Account Please Try Again...")
        models.left_id.objects.get(link=self.user, username=self.left_username).delete()
        return HttpResponse("You Got 1 Genuine Followers")


def contact_us(request):
    name = request.POST['field_name']
    email = request.POST['field_email']
    subject = request.POST['subject']
    message = request.POST['msg']
    try:
        models.contact_us.objects.create(name=name, email=email, subject=subject, message=message)
    except EOFError:
        pass
    return redirect('index')  

def join_us(request):
    email = request.POST['join_mail']
    message = request.POST.get('optional_text') or None
    try:
        models.join_us.objects.create(email=email, message=message)
    except EOFError:
        pass
    return redirect('index')  
