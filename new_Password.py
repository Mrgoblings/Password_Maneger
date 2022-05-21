from PySide2 import QtCore, QtGui, QtWidgets
import resources_rc

MAX_LINE_EDIT = 250
MAX_WIDGET_SIZE = 450


class Ui_newPasswordContainer(object):
    def setupUi(self, newPasswordContainer, index):
        newPasswordContainer.setObjectName(f"newPasswordContainer_{index}")
        newPasswordContainer.resize(705, 469)
        font = QtGui.QFont()
        font.setPointSize(13)
        newPasswordContainer.setFont(font)
        newPasswordContainer.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        newPasswordContainer.setLayoutDirection(QtCore.Qt.LeftToRight)
        newPasswordContainer.setStyleSheet("QLineEdit{\n"
                                           "    background-color: rgb(154, 153, 150);\n"
                                           "}\n"
                                           "")
        self.verticalLayout = QtWidgets.QVBoxLayout(newPasswordContainer)
        self.verticalLayout.setObjectName(f"verticalLayout_{index}")
        self.newPasswordSubContainer = QtWidgets.QFrame(newPasswordContainer)
        self.newPasswordSubContainer.setMinimumSize(QtCore.QSize(MAX_WIDGET_SIZE, 0))
        self.newPasswordSubContainer.setMaximumSize(QtCore.QSize(MAX_WIDGET_SIZE, 300))
        self.newPasswordSubContainer.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.newPasswordSubContainer.setStyleSheet("#newPasswordSubContainer{\n"
                                                   "    border : 0px solid blue;\n"
                                                   "    border-bottom:2px dashed rgb(255, 255, 255);\n"
                                                   "}")
        self.newPasswordSubContainer.setObjectName(f"newPasswordSubContainer_{index}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.newPasswordSubContainer)
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(f"verticalLayout_2_{index}")

        # sait widget
        self.sait_widget = QtWidgets.QWidget(self.newPasswordSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sait_widget.sizePolicy().hasHeightForWidth())
        self.sait_widget.setSizePolicy(sizePolicy)
        self.sait_widget.setMinimumSize(QtCore.QSize(MAX_WIDGET_SIZE, 0))
        self.sait_widget.setMaximumSize(QtCore.QSize(MAX_WIDGET_SIZE, 16777215))
        self.sait_widget.setObjectName(f"sait_widget_{index}")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.sait_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(f"horizontalLayout_{index}")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sait_label = QtWidgets.QLabel(self.sait_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sait_label.setFont(font)
        self.sait_label.setObjectName(f"sait_label_{index}")
        self.horizontalLayout.addWidget(self.sait_label, 0, QtCore.Qt.AlignRight)

        self.sait_input = QtWidgets.QLineEdit(self.sait_widget)
        self.sait_input.setMinimumSize(QtCore.QSize(MAX_LINE_EDIT, 28))
        self.sait_input.setMaximumSize(QtCore.QSize(MAX_LINE_EDIT, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sait_input.setFont(font)
        self.sait_input.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sait_input.setStyleSheet("")
        self.sait_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.sait_input.setObjectName(f"sait_input_{index}")
        self.horizontalLayout.addWidget(self.sait_input)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/clipboard.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.sait_copy_btn = QtWidgets.QPushButton(self.sait_widget)
        self.sait_copy_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sait_copy_btn.setText("")
        self.sait_copy_btn.setIcon(icon)
        self.sait_copy_btn.setIconSize(QtCore.QSize(24, 24))
        self.sait_copy_btn.setObjectName(f"sait_copy_btn_{index}")
        self.horizontalLayout.addWidget(self.sait_copy_btn)

        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.sait_widget)

        # login_name widget
        self.login_name_widget = QtWidgets.QWidget(self.newPasswordSubContainer)
        self.login_name_widget.setMinimumSize(QtCore.QSize(MAX_WIDGET_SIZE, 0))
        self.login_name_widget.setMaximumSize(QtCore.QSize(MAX_WIDGET_SIZE, 16777215))
        self.login_name_widget.setObjectName(f"login_name_widget_{index}")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.login_name_widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(f"horizontalLayout_2_{index}")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)

        self.login_name_label = QtWidgets.QLabel(self.login_name_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.login_name_label.setFont(font)
        self.login_name_label.setObjectName(f"login_name_label_{index}")
        self.horizontalLayout_2.addWidget(self.login_name_label, 0, QtCore.Qt.AlignRight)

        self.login_name_input = QtWidgets.QLineEdit(self.login_name_widget)
        self.login_name_input.setMinimumSize(QtCore.QSize(MAX_LINE_EDIT, 28))
        self.login_name_input.setMaximumSize(QtCore.QSize(MAX_LINE_EDIT, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.login_name_input.setFont(font)
        self.login_name_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.login_name_input.setObjectName(f"login_name_input_{index}")
        self.horizontalLayout_2.addWidget(self.login_name_input, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)

        self.login_copy_btn = QtWidgets.QPushButton(self.login_name_widget)
        self.login_copy_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_copy_btn.setText("")
        self.login_copy_btn.setIcon(icon)
        self.login_copy_btn.setIconSize(QtCore.QSize(24, 24))
        self.login_copy_btn.setObjectName(f"login_copy_btn_{index}")
        self.horizontalLayout_2.addWidget(self.login_copy_btn)

        spacerItem3 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.login_name_widget)

        # password widget
        self.password_widget = QtWidgets.QWidget(self.newPasswordSubContainer)
        self.password_widget.setMinimumSize(QtCore.QSize(MAX_WIDGET_SIZE, 0))
        self.password_widget.setMaximumSize(QtCore.QSize(MAX_WIDGET_SIZE, 16777215))
        self.password_widget.setObjectName(f"password_widget_{index}")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.password_widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(f"horizontalLayout_3_{index}")

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)

        self.password_label = QtWidgets.QLabel(self.password_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.password_label.setFont(font)
        self.password_label.setObjectName(f"password_label_{index}")
        self.horizontalLayout_3.addWidget(self.password_label, 0, QtCore.Qt.AlignRight)

        self.password_input = QtWidgets.QLineEdit(self.password_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_input.sizePolicy().hasHeightForWidth())
        self.password_input.setSizePolicy(sizePolicy)
        self.password_input.setMinimumSize(QtCore.QSize(MAX_LINE_EDIT, 28))
        self.password_input.setMaximumSize(QtCore.QSize(MAX_LINE_EDIT, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.password_input.setFont(font)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName(f"password_input_{index}")
        self.horizontalLayout_3.addWidget(self.password_input, 0, QtCore.Qt.AlignHCenter)

        self.password_copy_btn = QtWidgets.QPushButton(self.password_widget)
        self.password_copy_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.password_copy_btn.setText("")
        self.password_copy_btn.setIcon(icon)
        self.password_copy_btn.setIconSize(QtCore.QSize(24, 24))
        self.password_copy_btn.setObjectName(f"password_copy_btn_{index}")
        self.horizontalLayout_3.addWidget(self.password_copy_btn, 0, QtCore.Qt.AlignLeft)

        self.password_visibility_btn = QtWidgets.QPushButton(self.password_widget)
        self.password_visibility_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.password_visibility_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/eye-off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.password_visibility_btn.setIcon(icon1)
        self.password_visibility_btn.isActive = True
        self.password_visibility_btn.setIconSize(QtCore.QSize(24, 24))
        self.password_visibility_btn.setObjectName(f"password_visibility_btn_{index}")
        self.horizontalLayout_3.addWidget(self.password_visibility_btn, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.password_widget, 0, QtCore.Qt.AlignLeft)

        self.submit_btn = QtWidgets.QPushButton(self.newPasswordSubContainer)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.submit_btn.setFont(font)
        self.submit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_btn.setStyleSheet("background-color: rgb(222, 221, 218);\n"
                                      "color: rgb(0, 0, 0); padding: 3px; border:1px solid black")
        self.submit_btn.setObjectName("submit_btn")
        self.verticalLayout_2.addWidget(self.submit_btn, 0, QtCore.Qt.AlignRight)

        self.verticalLayout.addWidget(self.newPasswordSubContainer, 0, QtCore.Qt.AlignTop)

        self.retranslateUi(newPasswordContainer)
        QtCore.QMetaObject.connectSlotsByName(newPasswordContainer)

    def retranslateUi(self, newPasswordContainer):
        _translate = QtCore.QCoreApplication.translate
        newPasswordContainer.setWindowTitle(_translate("newPasswordContainer", "Form"))
        self.sait_label.setText(_translate("newPasswordContainer", "Sait: "))
        self.login_name_label.setText(_translate("newPasswordContainer", "Login name: "))
        self.password_label.setText(_translate("newPasswordContainer", "Password: "))
        self.submit_btn.setText(_translate("newPasswordContainer", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newPassword = QtWidgets.QWidget()
    ui = Ui_newPasswordContainer()
    ui.setupUi(newPassword)
    newPassword.show()
    sys.exit(app.exec_())
