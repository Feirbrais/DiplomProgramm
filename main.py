import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from gui import NewPassWindow, NewLoginWindow, MainWindow, LoginWindow, newStatusWindow, DeleteUserWindow, AddUserWindow
import dbFunctions#, monitoring
from PyQt5.QtGui import  QStandardItemModel,QStandardItem

class IdentifiedUser:
    id = ''
    login = ''
    password = ''
    status = ''

    @staticmethod
    def lievUser():
        IdentifiedUser.id = ''
        IdentifiedUser.login = ''
        IdentifiedUser.password = ''
        IdentifiedUser.status = ''
        
#mainWindow
class MainWindowSpace(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):

    PassView = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #title options and buttons
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.exitButton.clicked.connect(sys.exit)
        self.scrollDownButton.clicked.connect(self.showMinimized)
        self.SaveNewLoginButton.hide() 
        self.pushButton_2.hide() #saveNewPasswordButton
        self.lineEdit_2.setEchoMode(self.lineEdit_2.Password)
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.ProfileOpenButton.setFocus()
        self.ProfilesControlGroupBox.hide()

        #menu buttons
        self.ExitProfileButton.clicked.connect(self.LoginWindowSpaceOpen)
        self.ProfileredactorOpenButton.clicked.connect(self.OpenProfileRedactorGropBox)
        self.ProfileOpenButton.clicked.connect(self.OpenProfileGropBox)
        #Password and login redaction buttons
        self.RedactLoginForUserButton.clicked.connect(self.OpenRedactionLogin)
        self.RedactPassForUser.clicked.connect(self.OpenRedactionPassword)
        self.RedactStatusForUserButton.clicked.connect(self.OpenRedactionStatus)
        self.DeleteUserButton.clicked.connect(self.OpenDeleteUser)
        self.AddNewUserButton.clicked.connect(self.OpenAddUser)

    #open windows buttons
    def OpenAddUser(self):
        self.newuserwindow = AddUserWindowSpace()
        self.newuserwindow.show()

    def OpenRedactionPassword(self):
        self.newpasswindow = NewPassWindowSpace()
        self.newpasswindow.show()

    def OpenRedactionLogin(self):
        self.newlogwindow = NewLoginWindowSpace()
        self.newlogwindow.show()

    def OpenRedactionStatus(self):
        self.newstatuswindow = NewStatusWindowSpace()
        self.newstatuswindow.show()
    
    def OpenDeleteUser(self):
        self.deleteuserwindow = DeleteUserWindowSpace()
        self.deleteuserwindow.show()

    #open pages buttons
    def OpenProfileGropBox(self):
        self.ProfilesControlGroupBox.hide()
        self.ProfileGroupBox.show()

    def OpenProfileRedactorGropBox(self):
        self.ProfileGroupBox.hide()
        self.ProfilesControlGroupBox.show()
        self.tableCraft()

    #
    def tableCraft(self):
        data = dbFunctions.getUsersDataFoTable()
        statusNames = {1: 'Пользователь', 0: "Админ"}

        self.model = QStandardItemModel(3,len(data))
        self.model.setHorizontalHeaderLabels(['id','логин','статус'])
        for row in range(len(data)):
            self.model.setItem(row,0,QStandardItem(str(data[row][0])))
            self.model.setItem(row,1,QStandardItem(data[row][1]))
            self.model.setItem(row,2,QStandardItem(statusNames.get(data[row][3])))
        self.usersTableView.setModel(self.model)
        
    def SaveNewLogin(self):
        login = self.lineEdit.text()
        if login !='':
            dbFunctions.SaveNewLogin(login, IdentifiedUser.id)
            IdentifiedUser.login = login
            self.lineEdit.setEnabled(False)
            self.SaveNewLoginButton.hide()

    def SaveNewPassword(self):
        password = self.loginEdit_2.text()
        if password !='':
            dbFunctions.SaveNewLogin(password, IdentifiedUser.id)
            IdentifiedUser.password = password
            self.lineEdit_2.setEnabled(False)
            self.pushButton_2.hide()

    def setPassViewFormat(self):
        if MainWindowSpace.PassView:
            self.lineEdit_2.setEchoMode(self.lineEdit_2.Password)
            MainWindowSpace.PassView = False
        else:
            self.lineEdit_2.setEchoMode(self.lineEdit_2.Normal)
            MainWindowSpace.PassView = True

    def LoginWindowSpaceOpen(self):
        self.loginwindow = LoginWindowSpace()
        self.loginwindow.show()
        IdentifiedUser.lievUser()
        self.close()
    
    def statusInformationCheck(self):
        if IdentifiedUser.status == '0':
            self.StatusLabel.setText('Админ')
        elif IdentifiedUser.status == '1':
            self.StatusLabel.setText('Пользователь')
            self.ProfileredactorOpenButton.hide()
            #monitoring.startMonitoring()
        self.lineEdit.setText(IdentifiedUser.login)
        self.lineEdit_2.setText(IdentifiedUser.password)

#AddUserWindow
class AddUserWindowSpace(QtWidgets.QMainWindow, AddUserWindow.Ui_AddUserWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #title options and buttons
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.exitButton.clicked.connect(self.close)
        self.scrollDownButton.clicked.connect(self.showMinimized)
        self.loginErrorLabel.hide()
        self.passwordEdit.setEchoMode(self.passwordEdit.Password)

        #main buttons
        self.registrationButton.clicked.connect(self.RegistrationNewUser)
    
    def RegistrationNewUser(self):
        login = self.loginEdit.text()
        password = self.passwordEdit.text()
        if dbFunctions.UserCheck(login) and login !='' and password != '':
            dbFunctions.NewUserRegistration(login, password)
            self.MainWindowSpaceOpen()
        else:
            self.loginErrorLabel.setText('Пользователь с таким именем уже зарегистрирован')
            self.loginErrorLabel.show()

#DeleteUserWindow
class DeleteUserWindowSpace(QtWidgets.QMainWindow, DeleteUserWindow.Ui_DeleteUserWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #title options and buttons
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.exitButton.clicked.connect(self.close)
        self.scrollDownButton.clicked.connect(self.showMinimized)

        # #main buttons
        self.createButton.clicked.connect(self.DeleteUser)
    
    def DeleteUser(self):
        id = self.idEdit.text()
        if dbFunctions.CheckStatusOrRealisticUser(id):
            dbFunctions.delUser(id)

#NewStatusWindow
class NewStatusWindowSpace(QtWidgets.QMainWindow, newStatusWindow.Ui_NewStatusWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #title options and buttons
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.exitButton.clicked.connect(self.close)
        self.scrollDownButton.clicked.connect(self.showMinimized)

        # #main buttons
        self.loginButton.clicked.connect(self.SetNewStatus)
    
    def SetNewStatus(self):
        id = self.idEdit.text()
        if dbFunctions.CheckStatusOrRealisticUser(id):
            dbFunctions.SaveNewStatus(id)

#NewPassWindow
class NewPassWindowSpace(QtWidgets.QMainWindow, NewPassWindow.Ui_NewPassWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #title options and buttons
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.exitButton.clicked.connect(self.close)
        self.scrollDownButton.clicked.connect(self.showMinimized)

        # #main buttons
        self.newPassButton.clicked.connect(self.CreateNewPass)
    
    def CreateNewPass(self):
        id = self.idEdit.text()
        if dbFunctions.CheckStatusOrRealisticUser(id):
            password = self.passwordEdit.text()
            dbFunctions.SaveNewPassword(password, id)

#NewLoginWindow
class NewLoginWindowSpace(QtWidgets.QMainWindow, NewLoginWindow.Ui_NewLoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #title options and buttons
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.exitButton.clicked.connect(self.close)
        self.scrollDownButton.clicked.connect(self.showMinimized)

        # #main buttons
        self.newPassButton.clicked.connect(self.CreateNewLogin)

    def CreateNewlogin(self):
        id = self.idEdit.text()
        if dbFunctions.CheckStatusOrRealisticUser(id):
            log = self.passwordEdit.text()
            dbFunctions.SaveNewPassword(log, id)
    
    def CreateNewLogin(self):
        id = self.idEdit.text()
        if dbFunctions.CheckStatusOrRealisticUser(id):
            password = self.passwordEdit.text()
            #dbFunctions.SaveNewPassword(password, id)

#LoginWindow
class LoginWindowSpace(QtWidgets.QMainWindow, LoginWindow.Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #title options and buttons
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.exitButton.clicked.connect(sys.exit)
        self.scrollDownButton.clicked.connect(self.showMinimized)
        self.loginErrorLabel.hide()
        self.passwordEdit.setEchoMode(self.passwordEdit.Password)

        #main buttons
        self.loginButton.clicked.connect(self.MainWindowSpaceOpen)
        self.registrationButton.clicked.connect(self.RegistrationNewUser)

    def MainWindowSpaceOpen(self):
        login = self.loginEdit.text()
        password = self.passwordEdit.text()
        if dbFunctions.LoginPasswordCheck(login, password):
            self.mainwindow = MainWindowSpace()
            self.mainwindow.show()
            IdentifiedUser.id, IdentifiedUser.login, IdentifiedUser.password, IdentifiedUser.status = dbFunctions.getUserInformation(login, password)
            self.close()
            self.mainwindow.statusInformationCheck()
        else:
            self.loginErrorLabel.setText('Неверный логин или пароль')
            self.loginErrorLabel.show()
    
    def RegistrationNewUser(self):
        login = self.loginEdit.text()
        password = self.passwordEdit.text()
        if dbFunctions.UserCheck(login) and login !='' and password != '':
            dbFunctions.NewUserRegistration(login, password)
            self.MainWindowSpaceOpen()
        else:
            self.loginErrorLabel.setText('Пользователь с таким именем уже зарегистрирован')
            self.loginErrorLabel.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindowSpace()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()