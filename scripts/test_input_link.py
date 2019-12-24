from base.base_driver import init_driver
from page.display_page import DisplayPage
from page.browser_page import BrowserPage


class TestDisplay:

    def setup(self):
        self.driver = init_driver(1)
        self.browser_page = BrowserPage(self.driver)

    def test_mobile_display_input(self):
        self.driver.implicitly_wait(30)
        self.browser_page.click_search_button_text()
        self.browser_page.input_input_text_button('hao123')
        self.browser_page.click_search_button_tex()
        # 点击蓝牙
        # 点击手机名称
        # 输入文字
        # 点击返回
        # self.display_page.click_blue_tooth()
        # self.display_page.click_name()
        # self.display_page.send_keys_name(text=1)


        # self.driver.find_element_by_xpath('//android.widget.TextView[@text="蓝牙"]').click()
        # self.driver.find_element_by_id('miui:id/value_right').click()
        # self.driver.find_element_by_id('com.android.settings:id/device_name').send_keys(1)


