from bs4 import BeautifulSoup
import requests
import json
import os
import csv
import lxml.html.clean
import re


##HEY IGNORE MOST OF THE TOP CODE - ITS NOT CLEAN AND USER FRIENDLY - THIS IS SLOPPY WORK ON MY PART- 
##ALL CLEANME is doing is cleaning up the HTML RESULTS and STRIPPING THE SCRIPT / CSS CODE 

def cleanme(content):
    cleaner = lxml.html.clean.Cleaner(
        allow_tags=[],
        remove_unknown_tags=True,
        style=True,
    )
    html = lxml.html.document_fromstring(content)
    html_clean = cleaner.clean_html(html)
    return html_clean.text_content().strip()


headers = {
    'authority': 'accounts.google.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-gpc': '1',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://www.realtor.com/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__Secure-3PSID=HggQI6GDgH1aWdTfLQLgss1E26g4-jYoUWIrTPn-gZz5hTrajoG13XcjAy4WK2jJIyI3og.; __Host-3PLSID=doritos|o.admin.google.com|o.calendar.google.com|o.groups.google.com|o.mail.google.com|o.meet.google.com|o.myaccount.google.com|o.passwords.google.com|o.photos.google.com|o.remotedesktop.google.com|o.takeout.google.com|s.blogger|s.youtube:HggQI8xKeBwf3jpEtWMHHvNga-Cd5gaC-SYuLVcIrZLnlXJnGqRSdu3ZTiJqVFIZekCmjA.; __Secure-3PAPISID=RDYi1ll9eWMMXtTB/Ad6yzr8msjakww5kh; NID=511=tc_Ij0X4c5_gTb20dfIBE3a7Bmt5aLjYK0_MOzlkf_xG4F9Ql4BJjy-SMAxUITwF9_qtz4cvFu2MpVr1stF1nEhQ0SslvBQqRGxC6QxCo_NuKQYNmSsVpZdICRoiiI1toNXKWkMAXt7OI_eGDj4YiCJirgCoEt-j_5H6o0lcV4lbw_MxhDrXKyzRu8Vk-6jKq9L5lZL7bC_IiZ-DJV60BzMwwDt5Bx1DWgL0k5iHoGlQn5Q-OaKEdCQ2MiGH5He5UODdMfPaAENgdR14ejtQJtBv3tS6KQK8Hu9PZApRXDdp4IBTAw-0O7GfXXQS6gS7ZIPjGgK4_6BUC_aLvkxCkBwftcVUcIhV7fRbdMA; 1P_JAR=2022-03-08-09; __Secure-3PSIDCC=AJi4QfGX72f3WspmIMheqXXkyt-R27YO3F45Kx-37k58dujfqeJhRoEl3KYCQNYkNz4RkIakYd0',
}

params = (
    ('client_id', '1077613200872-2643uknuh1i8rfjgjd0jrkmm3frqqdo9.apps.googleusercontent.com'),
    ('auto_select', 'true'),
    ('ux_mode', 'popup'),
    ('ui_mode', 'card'),
    ('context', 'use'),
    ('nonce', 'dWM5NGNnYTV2NQ==1646732803546'),
    ('as', '+Wiy0ekh+r05yHF9mIdMBQ'),
    ('channel_id', '6b9462e15f6dd4dee321f6d8288ed44196419dd85c081977efef17d912b3df63'),
    ('origin', 'https://www.realtor.com'),
)


##MAGIC IS HERE  -  WE TAKE THE URL & SEARCH, and then PARSE THE HTML - THEN FOR EXTRA FUN 
##WE ASSIGNED A VARIABLE TO OUR SEARCH and ADDED USER INPUT!

city = input("search city here: ")
print(f"You are searching for Condos in {city}, good choice!")
url = f"https://www.realtor.com/realestateandhomes-search/{city}_CA/type-condo/price-na-300000"
req = requests.get(url, headers=headers, params=params)
soup = BeautifulSoup(req.content, 'html.parser')
dump = soup.find_all("div", class_="type-srp-result")
print("Dumping results to console!")
cleaned = cleanme(str(dump))
print(cleaned)
