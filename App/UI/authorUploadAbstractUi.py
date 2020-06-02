
from PyQt5 import QtCore, QtGui, QtWidgets

from UI.service import Service


class uploadAbstractUi(object):

    def uploadAbstract(self):
        paperName = self.paperNameLine.text()
        keywords = self.keywordsLine.text().split(',')
        topics = self.topicsLine.text().split(',')
        authors = self.authorsLine.text().split(',')
        Service().uploadAbstractCheck(paperName, keywords, topics, authors)


    def setupUi(self, uploadAbstractWindow):
        uploadAbstractWindow.setObjectName("uploadAbstractWindow")
        uploadAbstractWindow.resize(599, 271)
        self.formLayoutWidget = QtWidgets.QWidget(uploadAbstractWindow)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 0, 571, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.paperNameLine = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.paperNameLine.setObjectName("paperNameLine")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.paperNameLine)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.keywordsLine = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.keywordsLine.setObjectName("keywordsLine")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.keywordsLine)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.topicsLine = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.topicsLine.setObjectName("topicsLine")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.topicsLine)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.authorsLine = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.authorsLine.setObjectName("authorsLine")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.authorsLine)
        self.verticalLayoutWidget = QtWidgets.QWidget(uploadAbstractWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 160, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.submitPaperBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitPaperBtn.sizePolicy().hasHeightForWidth())
        self.submitPaperBtn.setSizePolicy(sizePolicy)
        self.submitPaperBtn.setObjectName("submitPaperBtn")
        self.verticalLayout.addWidget(self.submitPaperBtn)

        self.retranslateUi(uploadAbstractWindow)
        self.submitPaperBtn.clicked.connect(self.uploadAbstract)
        self.submitPaperBtn.clicked.connect(uploadAbstractWindow.close)

        QtCore.QMetaObject.connectSlotsByName(uploadAbstractWindow)

    def retranslateUi(self, uploadAbstractWindow):
        _translate = QtCore.QCoreApplication.translate
        uploadAbstractWindow.setWindowTitle(_translate("uploadAbstractWindow", "Form"))
        self.label_2.setText(_translate("uploadAbstractWindow", "            Paper Name                    "))
        self.label_3.setText(_translate("uploadAbstractWindow", "             Keywords                   "))
        self.label.setText(_translate("uploadAbstractWindow", "            Topics"))
        self.label_4.setText(_translate("uploadAbstractWindow", "            Authors"))
        self.submitPaperBtn.setText(_translate("uploadAbstractWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uploadAbstractWindow = QtWidgets.QWidget()
    ui = uploadAbstractUi()
    ui.setupUi(uploadAbstractWindow)
    uploadAbstractWindow.show()
    sys.exit(app.exec_())
