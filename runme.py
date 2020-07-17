from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
from django.conf import settings
import os
path_of_file = os.path.join(settings.BASE_DIR, 'static')

chromeOptions = Options()
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--disable-gpu")
chromeOptions.add_argument("--disable-dev-shm-usage")
chromeOptions.add_argument("--disable-dev-sha-usage")
chromeOptions.add_argument("--no-sandbox")

drivers = []
uname_block = [
            'kalmesh.gpt123'
]
# uname_block = [
#             'kalmesh.gpt123',
#             'paryan456',
#             'gulabosaho',
#             'akshaysharma9537',
#             'ruhilohariwal',
#             'sritesh009',
#             'abhinashtudu',
#             'azadaslam7',
#             '5arohisingh',
#             'dhirajsaho',
#             'ankit95678',
#             'keshulohariwal',
#             'harishagarwal90',
#             '3aceboyz',
#             'aman.gpt876',
#             'rohit.sharma737',
#             'niraj.saw939',
#             'rahul_gorai7',
#             'satyamshivam373',
#             'banajiajay'
# ]

if drivers != []:
    pass
else:
    for i in uname_block:
        chromeOptions.add_argument("user-data-dir={}".format(path_of_file+'/profiles/'+i))
        x = webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
        drivers.append(x)
        x.get("https://instagram.com/")
        sleep(1)
        print("Logged In With " + i)