# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpeakerChooseSectionPopUp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SpeakerChooseSectionPopUp(object):
    def setupUi(self, SpeakerChooseSectionPopUp):
        SpeakerChooseSectionPopUp.setObjectName("SpeakerChooseSectionPopUp")
        SpeakerChooseSectionPopUp.resize(320, 456)
        self.SectionsList = QtWidgets.QListWidget(SpeakerChooseSectionPopUp)
        self.SectionsList.setGeometry(QtCore.QRect(10, 40, 300, 360))
        self.SectionsList.setObjectName("SectionsList")
        self.label = QtWidgets.QLabel(SpeakerChooseSectionPopUp)
        self.label.setGeometry(QtCore.QRect(10, 10, 130, 30))
        self.label.setObjectName("label")
        self.chooseBtn = QtWidgets.QPushButton(SpeakerChooseSectionPopUp)
        self.chooseBtn.setGeometry(QtCore.QRect(80, 410, 160, 40))
        self.chooseBtn.setObjectName("chooseBtn")

        self.retranslateUi(SpeakerChooseSectionPopUp)

        ###POP UP CLOSE --> IMPORT SAVE
        self.chooseBtn.clicked.connect(SpeakerChooseSectionPopUp.close)
        ###
        QtCore.QMetaObject.connectSlotsByName(SpeakerChooseSectionPopUp)

    def retranslateUi(self, SpeakerChooseSectionPopUp):
        _translate = QtCore.QCoreApplication.translate
        SpeakerChooseSectionPopUp.setWindowTitle(_translate("SpeakerChooseSectionPopUp", "Choose section"))
        self.label.setText(_translate("SpeakerChooseSectionPopUp", "Sections"))
        self.chooseBtn.setText(_translate("SpeakerChooseSectionPopUp", "Choose"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpeakerChooseSectionPopUp = QtWidgets.QWidget()
    ui = Ui_SpeakerChooseSectionPopUp()
    ui.setupUi(SpeakerChooseSectionPopUp)
    SpeakerChooseSectionPopUp.show()
    sys.exit(app.exec_())
