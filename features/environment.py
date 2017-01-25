# -*- coding: UTF-8 -*-
# ----------------------------------------------------------------------------
# File: environment.py
# Autor: Kosalram
# Date: 18-1-17
# ----------------------------------------------------------------------------

#from selenium import webdriver
from helpers import axl_prjconfig
from helpers import axl_drivers

def before_all(context):
    browsertype = axl_prjconfig.get_browser()
    context.driver = axl_drivers.switch_browser(browsertype)
    context.url = axl_prjconfig.get_url()
    context.driver.get(context.url)
    context.screenservloc = axl_prjconfig.screensever_location()

def after_all(context):
    context.driver.quit()

def before_step(context, step):
    context.step = step

