# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Feirbrais\Desktop\Diplom\gui\UI-files\NewPassWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewPassWindow(object):
    def setupUi(self, NewPassWindow):
        NewPassWindow.setObjectName("NewPassWindow")
        NewPassWindow.setWindowModality(QtCore.Qt.NonModal)
        NewPassWindow.setEnabled(True)
        NewPassWindow.resize(420, 230)
        NewPassWindow.setMinimumSize(QtCore.QSize(420, 230))
        NewPassWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        NewPassWindow.setWindowTitle("NetWatcher")
        NewPassWindow.setStatusTip("")
        NewPassWindow.setAccessibleName("")
        NewPassWindow.setAccessibleDescription("")
        NewPassWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(235, 235, 235);\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    border: 0px;\n"
"}\n"
"QLineEdit {\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QGroupBox#groupBox_3 QPushButton:hover {\n"
"    background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"QGroupBox#titleBox QPushButton {\n"
"    border: 0px;\n"
"}\n"
"QPushButton#exitButton:hover {\n"
"    background-color: rgb(255, 81, 46);\n"
"}\n"
"QPushButton#scrollDownButton:hover {\n"
"    background-color: rgb(174, 255, 250);\n"
"}\n"
"QLabel#loginErrorLabel {\n"
"    color: rgb(255, 85, 0);\n"
"}\n"
"")
        NewPassWindow.setWindowFilePath("")
        NewPassWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(NewPassWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(420, 230))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleBox = QtWidgets.QGroupBox(self.centralwidget)
        self.titleBox.setMaximumSize(QtCore.QSize(16777215, 45))
        self.titleBox.setTitle("")
        self.titleBox.setObjectName("titleBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.titleBox)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.titleBox)
        self.label_4.setMinimumSize(QtCore.QSize(36, 36))
        self.label_4.setMaximumSize(QtCore.QSize(36, 36))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:\\Users\\Feirbrais\\Desktop\\Diplom\\gui\\UI-files\\imgs/titleIcon.png"))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.titleBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.scrollDownButton = QtWidgets.QPushButton(self.titleBox)
        self.scrollDownButton.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.scrollDownButton.setFont(font)
        self.scrollDownButton.setObjectName("scrollDownButton")
        self.horizontalLayout_2.addWidget(self.scrollDownButton)
        self.exitButton = QtWidgets.QPushButton(self.titleBox)
        self.exitButton.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout_2.addWidget(self.exitButton)
        self.verticalLayout.addWidget(self.titleBox)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(420, 60))
        self.groupBox.setStyleSheet("border-color: rgb(85, 170, 127);\n"
"border-bottom-color: rgb(85, 170, 127);\n"
"border-right-color: rgb(85, 170, 127);\n"
"border-top-color: rgb(85, 170, 127);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(420, 80))
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setMinimumSize(QtCore.QSize(130, 0))
        self.label_2.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.idEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.idEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idEdit.setFont(font)
        self.idEdit.setObjectName("idEdit")
        self.gridLayout_2.addWidget(self.idEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setMinimumSize(QtCore.QSize(130, 0))
        self.label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.passwordEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.passwordEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordEdit.setFont(font)
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout_2.addWidget(self.passwordEdit, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(420, 40))
        self.groupBox_3.setStyleSheet("")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newPassButton = QtWidgets.QPushButton(self.groupBox_3)
        self.newPassButton.setMinimumSize(QtCore.QSize(0, 30))
        self.newPassButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.newPassButton.setObjectName("newPassButton")
        self.horizontalLayout.addWidget(self.newPassButton)
        self.verticalLayout.addWidget(self.groupBox_3)
        NewPassWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewPassWindow)
        QtCore.QMetaObject.connectSlotsByName(NewPassWindow)

    def retranslateUi(self, NewPassWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("NewPassWindow", "NetInspector"))
        self.scrollDownButton.setText(_translate("NewPassWindow", "—"))
        self.exitButton.setText(_translate("NewPassWindow", "×"))
        self.label.setText(_translate("NewPassWindow", "Изменение пароля"))
        self.label_2.setText(_translate("NewPassWindow", "Id пользователя:"))
        self.label_3.setText(_translate("NewPassWindow", "Новый пароль:"))
        self.newPassButton.setText(_translate("NewPassWindow", "Задать новый пароль"))