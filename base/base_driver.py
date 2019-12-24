from appium import webdriver


def init_driver(name):
    # 1 表示手机是A37m
    if name == 1:
        caps = {"platformName": "Android", "deviceName": "NJLBYHRS4DU4AIBM", "appPackage": "com.android.browser",
                "appActivity": "com.android.browser.BrowserActivity", "noReset": "True", "unicodeKeyboard": "True",
                "resetKeyboard": "True"}

        return webdriver.Remote("http://localhost:4723/wd/hub", caps)

