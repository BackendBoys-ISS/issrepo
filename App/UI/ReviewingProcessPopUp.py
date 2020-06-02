
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReviewingProcessPopUp(object):
    def setupUi(self, ReviewingProcessPopUp):
        ReviewingProcessPopUp.setObjectName("ReviewingProcessPopUp")
        ReviewingProcessPopUp.resize(777, 519)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ReviewingProcessPopUp)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 39, 211, 471))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(ReviewingProcessPopUp)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(230, 40, 221, 471))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_2.addWidget(self.listWidget_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(ReviewingProcessPopUp)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(460, 40, 301, 471))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listWidget_3 = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget_3.setObjectName("listWidget_3")
        self.horizontalLayout_3.addWidget(self.listWidget_3)
        self.label = QtWidgets.QLabel(ReviewingProcessPopUp)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ReviewingProcessPopUp)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ReviewingProcessPopUp)
        self.label_3.setGeometry(QtCore.QRect(470, 20, 131, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(ReviewingProcessPopUp)
        QtCore.QMetaObject.connectSlotsByName(ReviewingProcessPopUp)

    def retranslateUi(self, ReviewingProcessPopUp):
        _translate = QtCore.QCoreApplication.translate
        ReviewingProcessPopUp.setWindowTitle(_translate("ReviewingProcessPopUp", "Reviewing process"))
        self.label.setText(_translate("ReviewingProcessPopUp", "Paper"))
        self.label_2.setText(_translate("ReviewingProcessPopUp", "Status"))
        self.label_3.setText(_translate("ReviewingProcessPopUp", "Reviewers"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReviewingProcessPopUp = QtWidgets.QWidget()
    ui = Ui_ReviewingProcessPopUp()
    ui.setupUi(ReviewingProcessPopUp)
    ReviewingProcessPopUp.show()
    sys.exit(app.exec_())
