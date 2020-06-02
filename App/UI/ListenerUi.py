
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListenerUi(object):
    def setupUi(self, ListenerUi):
        ListenerUi.setObjectName("ListenerUi")
        ListenerUi.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ListenerUi)
        self.centralwidget.setObjectName("centralwidget")
        self.sectionsList = QtWidgets.QListWidget(self.centralwidget)
        self.sectionsList.setGeometry(QtCore.QRect(10, 40, 380, 400))
        self.sectionsList.setObjectName("sectionsList")
        self.chosenSectionsList = QtWidgets.QListWidget(self.centralwidget)
        self.chosenSectionsList.setGeometry(QtCore.QRect(410, 40, 380, 400))
        self.chosenSectionsList.setObjectName("chosenSectionsList")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 140, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 20, 140, 20))
        self.label_2.setObjectName("label_2")
        self.addSectionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addSectionBtn.setGeometry(QtCore.QRect(10, 460, 150, 50))
        self.addSectionBtn.setObjectName("addSectionBtn")
        ListenerUi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ListenerUi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        ListenerUi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ListenerUi)
        self.statusbar.setObjectName("statusbar")
        ListenerUi.setStatusBar(self.statusbar)

        self.retranslateUi(ListenerUi)
        QtCore.QMetaObject.connectSlotsByName(ListenerUi)

    def retranslateUi(self, ListenerUi):
        _translate = QtCore.QCoreApplication.translate
        ListenerUi.setWindowTitle(_translate("ListenerUi", "MainWindow"))
        self.label.setText(_translate("ListenerUi", "Available sections"))
        self.label_2.setText(_translate("ListenerUi", "Your sections"))
        self.addSectionBtn.setText(_translate("ListenerUi", "Add section"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ListenerUi = QtWidgets.QMainWindow()
    ui = Ui_ListenerUi()
    ui.setupUi(ListenerUi)
    ListenerUi.show()
    sys.exit(app.exec_())
