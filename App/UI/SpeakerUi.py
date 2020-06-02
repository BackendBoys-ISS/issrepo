
from PyQt5 import QtCore, QtWidgets
from UI.SpeakerChooseSectionPopUp import Ui_SpeakerChooseSectionPopUp
from UI.UserType import UserType


class Ui_SpeakerUi(object):
    def openChoseSection(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SpeakerChooseSectionPopUp()
        self.ui.setupUi(self.window)
        self.window.show()

    def setUser(self, user: UserType):
        self.user = user

    def setupUi(self, SpeakerUi, user):
        self.setUser(user)
        SpeakerUi.setObjectName("SpeakerUi")
        SpeakerUi.resize(1024, 720)
        self.centralwidget = QtWidgets.QWidget(SpeakerUi)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 180, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.buttonsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.buttonsLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.yourReviewsBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.yourReviewsBtn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yourReviewsBtn.sizePolicy().hasHeightForWidth())
        self.yourReviewsBtn.setSizePolicy(sizePolicy)
        self.yourReviewsBtn.setMaximumSize(QtCore.QSize(400, 50))
        self.yourReviewsBtn.setObjectName("yourReviewsBtn")
        self.buttonsLayout.addWidget(self.yourReviewsBtn)
        self.reviewersList = QtWidgets.QListWidget(self.centralwidget)
        self.reviewersList.setGeometry(QtCore.QRect(200, 50, 256, 440))
        self.reviewersList.setObjectName("reviewersList")
        self.reviewContentText = QtWidgets.QTextEdit(self.centralwidget)
        self.reviewContentText.setGeometry(QtCore.QRect(470, 50, 540, 440))
        self.reviewContentText.setObjectName("reviewContentText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 30, 130, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 30, 130, 20))
        self.label_2.setObjectName("label_2")
        self.uploadNewPaperBtn = QtWidgets.QPushButton(self.centralwidget)
        self.uploadNewPaperBtn.setGeometry(QtCore.QRect(200, 510, 150, 50))
        self.uploadNewPaperBtn.setObjectName("uploadNewPaperBtn")
        self.uploadPresentationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.uploadPresentationBtn.setGeometry(QtCore.QRect(370, 510, 150, 50))
        self.uploadPresentationBtn.setObjectName("uploadPresentationBtn")
        self.chooseSectionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.chooseSectionBtn.setGeometry(QtCore.QRect(540, 510, 150, 50))
        self.chooseSectionBtn.setObjectName("chooseSectionBtn")
        SpeakerUi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SpeakerUi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        SpeakerUi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SpeakerUi)
        self.statusbar.setObjectName("statusbar")
        SpeakerUi.setStatusBar(self.statusbar)

        self.retranslateUi(SpeakerUi)

        ###OPEN CHOOSE SECTION POP UP
        self.chooseSectionBtn.clicked.connect(self.openChoseSection)
        QtCore.QMetaObject.connectSlotsByName(SpeakerUi)

    def retranslateUi(self, SpeakerUi):
        _translate = QtCore.QCoreApplication.translate
        SpeakerUi.setWindowTitle(_translate("SpeakerUi", "Speaker"))
        self.yourReviewsBtn.setText(_translate("SpeakerUi", "View paper"))
        self.label.setText(_translate("SpeakerUi", "Reviews"))
        self.label_2.setText(_translate("SpeakerUi", "Review content"))
        self.uploadNewPaperBtn.setText(_translate("SpeakerUi", "Upload new paper"))
        self.uploadPresentationBtn.setText(_translate("SpeakerUi", "Upload presentation"))
        self.chooseSectionBtn.setText(_translate("SpeakerUi", "Choose section"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpeakerUi = QtWidgets.QMainWindow()
    ui = Ui_SpeakerUi()
    ui.setupUi(SpeakerUi, UserType(False, True, True, "user1"))
    SpeakerUi.show()
    sys.exit(app.exec_())
