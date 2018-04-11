# coding=utf-8
from framework.base_page import BasePage


class LoginPage(BasePage):

    input_box1 = "id=>username"
    input_box2 = "id=>password"

    login_submit_btn = "id=>login"

    def type_username(self, text):
        self.type(self.input_box1, text)

    def type_password(self, text):
        self.type(self.input_box2, text)

    def send_submit_btn(self):
        self.click(self.login_submit_btn)

