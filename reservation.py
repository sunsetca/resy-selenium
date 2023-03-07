import json
from functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By

res_file = open("./settings/settings.json")
res_settings = json.load(res_file)
login_file = open('./settings/login_settings.json')
login_settings = json.load(login_file)
program_file = open('./settings/program_settings.json')
program_settings = json.load(program_file)

url = res_settings["site"] + res_settings["city"] + scrubUrl(res_settings["restaurant"]) + res_settings["date"] + res_settings["seats"]
reservation_times = relevantTimes(res_settings["time"])


driver = webdriver.Chrome()
driver.get(url)
title = driver.title
print(title)


driver.quit()