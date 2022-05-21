
# from PyQt5.QtWidgets import QApplication, QMainWindow
from Custom_Widgets.Widgets import *
import os
import sys

from crypt_decrypt import AESCipher

from interface import *
from new_Password import Ui_newPasswordContainer

import requests
import json


BASE = "http://127.0.0.1:5000/"
url = f"{BASE}api/lol"
headers = {'Content-type': 'application/json; charset=utf-8'}


class NewPassword(QWidget, Ui_newPasswordContainer):
    def __init__(self, index, parent=None):
        QWidget.__init__(self, parent=None)
        self.setupUi(self, index)


class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow=self)
        self.new_pass_json = []  # json format e.g. [{}, {}, {}]
        self.all_passwords = []
        self.cipher = AESCipher("1234")

        self.loading_mode = True

        loadJsonStyle(self, self.ui)

        self.render_old_passwords()

        self.show()

        #  Expand CentralMenu
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centralMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centralMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centralMenuContainer.expandMenu())
        # Close centralMenu
        self.ui.closeCentralMenuBtn.clicked.connect(lambda: self.ui.centralMenuContainer.collapseMenu())
        self.ui.addPassBtn.clicked.connect(lambda: self.insert_passwort())

    def insert_passwort(self):
        if self.is_there_empty_passwordContainer() and not self.loading_mode:
            self.password_activated("all", len(self.all_passwords) - 1)

            if self.is_there_empty_passwordContainer():
                raise AttributeError("Unfilled containers")

        new_pass = NewPassword(len(self.all_passwords))
        self.ui.verticalLayout_14.addWidget(new_pass, 3, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

        pass_len = len(self.all_passwords)

        # make them save param
        new_pass.sait_input.returnPressed.connect(lambda: self.password_activated("sait", pass_len))
        new_pass.login_name_input.returnPressed.connect(lambda: self.password_activated("login_name", pass_len))
        new_pass.password_input.returnPressed.connect(lambda: self.password_activated("password", pass_len))

        self.all_passwords.append(new_pass)

        if not self.loading_mode:
            self.new_pass_json.append({"sait": "", "login_name": "", "password": ""})
        new_pass.show()

    def password_activated(self, line_type, index):
        old_pass_dict = self.new_pass_json[index].copy()  # old_pass_dict: dict
        if line_type == "sait":
            self.new_pass_json[index]["sait"] = self.cipher.encrypt(self.all_passwords[index].sait_input.text())  # noqa
        elif line_type == "login_name":
            self.new_pass_json[index]["login_name"] = self.cipher.encrypt(self.all_passwords[index].login_name_input.text())  # noqa
        elif line_type == "password":
            self.new_pass_json[index]["password"] = self.cipher.encrypt(self.all_passwords[index].password_input.text())  # noqa
        elif line_type == "all":
            self.new_pass_json[index]["sait"] = self.cipher.encrypt(self.all_passwords[index].sait_input.text())  # noqa
            self.new_pass_json[index]["login_name"] = self.cipher.encrypt(self.all_passwords[index].login_name_input.text())  # noqa
            self.new_pass_json[index]["password"] = self.cipher.encrypt(self.all_passwords[index].password_input.text())  # noqa
        else:
            raise ValueError("given wrong argument line_type")
        print(self.new_pass_json)
        if self.cipher.encrypt("") not in old_pass_dict.values():  # noqa
            if self.cipher.encrypt("") not in self.new_pass_json[index] and old_pass_dict != self.new_pass_json[index]:
                temp_dict = dict(set(self.new_pass_json[index].items()) - set(old_pass_dict.items()))  # noqa
                print(f"temp_dict = {temp_dict}")
                for key, value in temp_dict.items():
                    old_pass_dict["which_attribute"] = key  # noqa
                    old_pass_dict["updated_attribute"] = value  # noqa
                    print(f"patchin {old_pass_dict}")
                    requests.patch(url, json.dumps(old_pass_dict), headers=headers)

        elif len(self.new_pass_json) != 0 and self.cipher.encrypt("") not in self.new_pass_json[index]:
            print("Sending lolypops")  # TODO remove or make smarter
            return requests.post(url, json.dumps(self.new_pass_json[index]), headers=headers).json()

    def render_old_passwords(self):
        self.new_pass_json = requests.get(url).json()

        if not isinstance(self.new_pass_json, list):
            exception = self.new_pass_json
            self.new_pass_json = []
            raise ConnectionError(exception)

        temp_pass_json = self.new_pass_json.copy()
        for elem in temp_pass_json:
            self.insert_passwort()
            self.all_passwords[len(self.all_passwords) - 1].sait_input.setText(self.cipher.decrypt(elem["sait"]))
            self.all_passwords[len(self.all_passwords) - 1].login_name_input.setText(self.cipher.decrypt(elem["login_name"]))
            self.all_passwords[len(self.all_passwords) - 1].password_input.setText(self.cipher.decrypt(elem["password"]))

        # end of function
        self.loading_mode = False

    def is_there_empty_passwordContainer(self):  # noqa
        print(self.new_pass_json)
        for pass_dict in self.new_pass_json:
            if "" in pass_dict.values():
                return True
        return False


if __name__ == "__main__":
    app = QApplication(sys.argv)  # noqa
    window = ApplicationWindow()
    sys.exit(app.exec_())

# commands to generate the python code from .ui and .qrc
# python3 -m PyQt5.uic.pyuic -x interface.ui -o interface.py
# pyside2-rcc resources.qrc -o resources_rc.py
