
# from PyQt5.QtWidgets import QApplication, QMainWindow
from Custom_Widgets.Widgets import *
import os
import sys

from crypt_decrypt import AESCipher

from interface import *
from new_Password import Ui_newPasswordContainer

import copy

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
        self.in_db_pass_json = []

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
        self.ui.addPassBtn.clicked.connect(lambda: self.insert_password())

    def insert_password(self):
        if self.in_db_pass_json != self.new_pass_json and not self.loading_mode:
            # print(set(self.in_db_pass_json)^set(self.new_pass_json))
            raise ValueError("Unsubmitted containers")

        new_pass = NewPassword(len(self.all_passwords))
        self.ui.verticalLayout_14.addWidget(new_pass, 3, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

        pass_len = len(self.all_passwords)

        # make them save param
        new_pass.sait_input.returnPressed.connect(lambda: self.password_activated("sait", pass_len))
        new_pass.login_name_input.returnPressed.connect(lambda: self.password_activated("login_name", pass_len))
        new_pass.password_input.returnPressed.connect(lambda: self.password_activated("password", pass_len))

        new_pass.sait_copy_btn.clicked.connect(lambda: self.copy_to_clipboard(new_pass.sait_input))
        new_pass.login_copy_btn.clicked.connect(lambda: self.copy_to_clipboard(new_pass.login_name_input))
        new_pass.password_copy_btn.clicked.connect(lambda: self.copy_to_clipboard(new_pass.password_input))

        new_pass.password_visibility_btn.clicked.connect(lambda: self.visibility_btn_clicked(new_pass))
        new_pass.submit_btn.clicked.connect(lambda: self.submit_btn_clicked(pass_len))

        self.all_passwords.append(new_pass)

        if not self.loading_mode:
            self.new_pass_json.append({"sait": self.cipher.encrypt(""), "login_name": self.cipher.encrypt(""), "password": self.cipher.encrypt("")})
        new_pass.show()

    def password_activated(self, line_type: str, index: int):
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
        print("the jsons:\n\n")
        print(self.new_pass_json[index])
        print(self.in_db_pass_json[index])

    def render_old_passwords(self):
        self.new_pass_json = requests.get(url).json()

        if not isinstance(self.new_pass_json, list):
            exception = self.new_pass_json
            self.new_pass_json = []
            raise ConnectionError(exception)

        for elem in self.new_pass_json:
            self.insert_password()
            self.all_passwords[len(self.all_passwords) - 1].sait_input.setText(self.cipher.decrypt(elem["sait"]))
            self.all_passwords[len(self.all_passwords) - 1].login_name_input.setText(self.cipher.decrypt(elem["login_name"]))
            self.all_passwords[len(self.all_passwords) - 1].password_input.setText(self.cipher.decrypt(elem["password"]))

        # end of function
        self.loading_mode = False
        self.in_db_pass_json = copy.deepcopy(self.new_pass_json)

    def is_there_empty_passwordContainer(self, index: int):  # noqa
        for elem in self.new_pass_json[index].values():
            if "" is self.cipher.decrypt(elem):
                return True
            print(f"elem = {elem}")
        return False

    def submit_btn_clicked(self, index: int):
        # if self.cipher.encrypt("") not in old_pass_dict[index].values():
        print(f"We are here at  index {index}")
        try:
            if not self.is_there_empty_passwordContainer(index) and self.in_db_pass_json[index] != self.new_pass_json[index]:
                temp_dict = dict(set(self.new_pass_json[index].items()) - set(self.in_db_pass_json[index].items()))
                print(f"temp_dict = {temp_dict}")
                response_dict = self.in_db_pass_json[index].copy()
                for key, value in temp_dict.items():
                    response_dict["which_attribute"] = key
                    response_dict["updated_attribute"] = value
                    print(f"patchin {response_dict}")
                    print(requests.patch(url, json.dumps(response_dict), headers=headers))
            else:
                print(self.new_pass_json[index])
                raise ValueError("Unable to submit")

        except IndexError:
            if len(self.new_pass_json) != 0 and not self.is_there_empty_passwordContainer(index):
                print("Sending lolypops")  # TODO remove or make smarter
                self.in_db_pass_json.append(self.new_pass_json[index].copy())
                return requests.post(url, json.dumps(self.new_pass_json[index]), headers=headers).json()
            else:
                print(self.new_pass_json[index])
                raise ValueError("Unable to submit")

    @staticmethod
    def visibility_btn_clicked(pass_container):
        icon = QIcon()
        if pass_container.password_visibility_btn.isActive:
            icon.addPixmap(QtGui.QPixmap(":/icons/icons/eye.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            pass_container.password_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            pass_container.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
            icon.addPixmap(QtGui.QPixmap(":/icons/icons/eye-off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pass_container.password_visibility_btn.isActive = not pass_container.password_visibility_btn.isActive
        pass_container.password_visibility_btn.setIcon(icon)

    @staticmethod
    def copy_to_clipboard(edit_line: QLineEdit):
        clipboard = QApplication.clipboard()
        clipboard.setText(edit_line.text(), mode=clipboard.Clipboard)
        print(f"Copying {edit_line.text()} to clipboard")


if __name__ == "__main__":
    app = QApplication(sys.argv)  # noqa
    window = ApplicationWindow()
    sys.exit(app.exec_())

# commands to generate the python code from .ui and .qrc
# python3 -m PyQt5.uic.pyuic -x interface.ui -o interface.py
# pyside2-rcc resources.qrc -o resources_rc.py
