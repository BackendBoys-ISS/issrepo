
from PyQt5 import QtCore, QtWidgets

from UI.UserType import UserType
from UI.authorUi import Ui_MainWindow
from UI.ListenerUi import Ui_ListenerUi
from UI.SpeakerUi import Ui_SpeakerUi
from UI.service import Service


class Ui_StackedWidget(object):

    def openListenerWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ListenerUi()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSpeakerWindow(self, username):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SpeakerUi()
        self.ui.setupUi(self.window, username)
        self.window.show()

    def openWindow(self, username): #Author
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window, username)

        self.window.show()

    def checkLogin(self):
        msg = QtWidgets.QMessageBox()

        if Service().loginCheck(self.emailLineEdit.text(), self.passwordLineEdit.text()) != 'not set':
            #msg.setText('success')
            #msg.exec_()
            username = UserType(False, False, False, 'user1')

            if  username.isListener == True:
                self.openListenerWindow()
            elif username.isSpeaker == True:
                self.openSpeakerWindow(username)
            else:
                self.openWindow(username)
            StackedWidget.close()
        else:
            msg.setText('incorrect credentials')
            msg.exec_()

    def createAccount(self):
        msg = QtWidgets.QMessageBox()

        if self.createAccountPwdLineEdit.text() != self.createAccountConfirmPwdLineEdit.text():
            msg.setText('passwords are not identical')
        elif self.createAccountNameLineEdit.text() == '' or self.createAccountEmailLineEdit.text() == '' or \
                                         self.createAccountPwdLineEdit.text() == '':
            msg.setText('empty field detected don\'t be an asshole (please give me a 10)')

        else:
            result = Service().createAccountCheck(self.createAccountNameLineEdit.text(), self.createAccountEmailLineEdit.text(),
                                         self.createAccountPwdLineEdit.text())
            msg.setText(result)
            self.createAccountPage.hide()
            self.mainPage.show()

        msg.exec_()


    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(640, 480)
        self.mainPage = QtWidgets.QWidget()
        self.mainPage.setObjectName("mainPage")
        self.loginButton = QtWidgets.QPushButton(self.mainPage)
        self.loginButton.setGeometry(QtCore.QRect(130, 330, 131, 61))
        self.loginButton.setObjectName("loginButton")
        self.createAccountButton = QtWidgets.QPushButton(self.mainPage)
        self.createAccountButton.setGeometry(QtCore.QRect(350, 330, 131, 61))
        self.createAccountButton.setObjectName("createAccountButton")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.mainPage)
        self.passwordLineEdit.setGeometry(QtCore.QRect(190, 230, 241, 31))
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("password")
        self.emailLineEdit = QtWidgets.QLineEdit(self.mainPage)
        self.emailLineEdit.setGeometry(QtCore.QRect(190, 140, 241, 31))
        self.emailLineEdit.setObjectName("email")
        self.label_7 = QtWidgets.QLabel(self.mainPage)
        self.label_7.setGeometry(QtCore.QRect(190, 120, 55, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.mainPage)
        self.label_8.setGeometry(QtCore.QRect(190, 210, 101, 16))
        self.label_8.setObjectName("label_8")
        StackedWidget.addWidget(self.mainPage)
        self.createAccountPage = QtWidgets.QWidget()
        self.createAccountPage.setObjectName("createAccountPage")
        self.label = QtWidgets.QLabel(self.createAccountPage)
        self.label.setGeometry(QtCore.QRect(190, 50, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.createAccountPage)
        self.label_2.setGeometry(QtCore.QRect(190, 130, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.createAccountPage)
        self.label_3.setGeometry(QtCore.QRect(190, 210, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.createAccountPage)
        self.label_4.setGeometry(QtCore.QRect(190, 290, 141, 16))
        self.label_4.setObjectName("label_4")
        self.confirmAccount = QtWidgets.QPushButton(self.createAccountPage)
        self.confirmAccount.setGeometry(QtCore.QRect(240, 367, 151, 41))
        self.confirmAccount.setObjectName("confirmAccount")
        self.backCreateAccount = QtWidgets.QPushButton(self.createAccountPage)
        self.backCreateAccount.setGeometry(QtCore.QRect(270, 430, 93, 28))
        self.backCreateAccount.setObjectName("backCreateAccount")
        self.createAccountNameLineEdit = QtWidgets.QLineEdit(self.createAccountPage)
        self.createAccountNameLineEdit.setGeometry(QtCore.QRect(190, 70, 241, 31))
        self.createAccountNameLineEdit.setObjectName("nameLineEdit")
        self.createAccountEmailLineEdit = QtWidgets.QLineEdit(self.createAccountPage)
        self.createAccountEmailLineEdit.setGeometry(QtCore.QRect(190, 150, 241, 31))
        self.createAccountEmailLineEdit.setObjectName("emailLineEdit")
        self.createAccountPwdLineEdit = QtWidgets.QLineEdit(self.createAccountPage)
        self.createAccountPwdLineEdit.setGeometry(QtCore.QRect(190, 230, 241, 31))
        self.createAccountPwdLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createAccountPwdLineEdit.setObjectName("passwordLineEdit")
        self.createAccountConfirmPwdLineEdit = QtWidgets.QLineEdit(self.createAccountPage)
        self.createAccountConfirmPwdLineEdit.setGeometry(QtCore.QRect(190, 310, 241, 31))
        self.createAccountConfirmPwdLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createAccountConfirmPwdLineEdit.setObjectName("confirmPasswordLineEdit")
        StackedWidget.addWidget(self.createAccountPage)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(0)
        self.createAccountButton.clicked.connect(self.mainPage.hide)
        self.createAccountButton.clicked.connect(self.createAccountPage.show)
        self.backCreateAccount.clicked.connect(self.createAccountPage.hide)
        self.backCreateAccount.clicked.connect(self.mainPage.show)


        ##LOGIN
        ###IMPLEMENT IF STATEMENT
        self.loginButton.clicked.connect(self.checkLogin)
        self.confirmAccount.clicked.connect(self.createAccount)
        #self.loginButton.clicked.connect(self.openWindow)
        #self.loginButton.clicked.connect(self.openListenerWindow)
        #self.loginButton.clicked.connect(self.openSpeakerWindow)
        #self.loginButton.clicked.connect(StackedWidget.close)

        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "Login"))
        self.loginButton.setText(_translate("StackedWidget", "Login"))
        self.createAccountButton.setText(_translate("StackedWidget", "Create Account"))
        self.label_7.setText(_translate("StackedWidget", "Email"))
        self.label_8.setText(_translate("StackedWidget", "Password"))
        self.label.setText(_translate("StackedWidget", "Enter your full name"))
        self.label_2.setText(_translate("StackedWidget", "Enter your email"))
        self.label_3.setText(_translate("StackedWidget", "Enter your password"))
        self.label_4.setText(_translate("StackedWidget", "Confirm your password"))
        self.confirmAccount.setText(_translate("StackedWidget", "Create Account"))
        self.backCreateAccount.setText(_translate("StackedWidget", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StackedWidget = QtWidgets.QStackedWidget()
    ui = Ui_StackedWidget()
    ui.setupUi(StackedWidget)
    StackedWidget.show()
    sys.exit(app.exec_())
