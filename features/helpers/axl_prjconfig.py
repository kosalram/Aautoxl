# -*- coding: UTF-8 -*-
# ----------------------------------------------------------------------------
# File: axl_prjconfig.py
# Autor: Kosalram
# Date: 18-1-17
# ----------------------------------------------------------------------------

import configparser
import os
import sys
import platform
from axl_browsers import Browsers


#projectRoot = "c:\Users\OT_KC\PycharmProjects\Maddy_Test"
projectRoot = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#projectRoot = os.path.dirname(os.path.abspath(__file__))

print("projectRoot=")
print(projectRoot)

def getConfig():
    configFilePath = os.path.join(projectRoot, "features", "axl_config.ini")
    configParser = configparser.RawConfigParser()
    configParser.read(configFilePath)
    return configParser

config = getConfig()

def get_setting(parent, key):
    return config.get(parent, key)

def get_browser():
    return Browsers.get_browser(get_setting("selenium", "driver"))

print("Driver Assigned =" + " "+ get_setting("selenium", "driver"))

def read_chromedriver_location():
    return os.path.join(projectRoot, "tools", get_chromedriver())

def get_chromedriver():
    #return "chromedriver.exe" if is_windows() else "chromedriver64" if is_64bit() else "chromedriver"
    return "chromedriver"

def read_internetexplorer_location():
    return os.path.join(projectRoot, "tools", get_IEdriver())

def get_IEdriver():
    #return "chromedriver.exe" if is_windows() else "chromedriver64" if is_64bit() else "chromedriver"
    return "IEDriverServer"

def get_url():
    return (get_setting("tests", "url"))

def screensever_location():
    return os.path.join(projectRoot, "reports\screenshots\\")

print("Screen Sever Location=" + " "+ screensever_location())

print("Driver Assigned =" + " "+ get_setting("selenium", "driver"))



