from appium import webdriver
from appium.options.android import UiAutomator2Options

from core.config import *

def get_driver():

    options = UiAutomator2Options()

    options.platform_name = PLATFORM_NAME
    options.device_name = DEVICE_NAME

    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY

    driver = webdriver.Remote(
        APPIUM_SERVER,
        options=options
    )

    return driver