# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine          #!!!!!!!!!!
from UrsalinkTestWeb.baidu_homepage import HomePage

class BaiduSearch(unittest.TestCase):


    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)


    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
       # self.driver.find_element_by_id('kw').send_keys('selenium')
       #self.driver.find_element_by_id('su').click()            #!!!!!!!!!!!
       # time.sleep(5)
        try:
            #assert 'selenium' in self.driver.title
            assert 'selenium' in homepage.get_page_title()
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

if __name__ == '__main__':
    unittest.main()
