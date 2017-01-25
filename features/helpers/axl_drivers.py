# -*- coding: UTF-8 -*-
# ----------------------------------------------------------------------------
# File: axl_config.ini
# Autor: Kosalram
# Date: 18-1-17
# ----------------------------------------------------------------------------


from axl_browsers import Browsers
from helpers import axl_prjconfig
import os
from selenium import webdriver

def get_chrome():
    chromedriver = axl_prjconfig.read_chromedriver_location()
    os.environ["webdriver.chrome.driver"] = chromedriver
    return webdriver.Chrome(chromedriver)


def get_ie():
    iedriver = axl_prjconfig.read_internetexplorer_location()
    os.environ["webdriver.ie.driver"] = iedriver
    return webdriver.Ie(iedriver)

def switch_browser(browser):
    return {Browsers.chrome: get_chrome, Browsers.internetexplorer: get_ie}.get(browser, lambda: webdriver.Firefox())()