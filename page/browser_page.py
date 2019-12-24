from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class BrowserPage(BaseAction):
    pass
    search_button_text = By.ID, 'com.android.browser:id/ayz',
    input_text_button = By.XPATH, '//android.widget.RelativeLayout[@resource-id="com.android.browser:id/b61"]/brow' \
                                  'ser.widget.EditText'
    click_search_button = By.ID, 'com.android.browser:id/zn'

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def click_search_button_text(self):
        self.click(self.search_button_text)

    def input_input_text_button(self, text):
        self.input_text(self.input_text_button, text)

    def click_search_button_tex(self):
        self.click(self.click_search_button)





