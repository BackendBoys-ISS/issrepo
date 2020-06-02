
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem

from UI.service import Service


class Ui_ReviewerResults(object):
    def openReviewerReviewsPage(self):
        from UI.ReviewerReviews import Ui_ReviewerReviews
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ReviewerReviews()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, ReviewerResults):
        ReviewerResults.setObjectName("ReviewerResults")
        ReviewerResults.resize(1024, 720)
        self.centralwidget = QtWidgets.QWidget(ReviewerResults)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 180, 221))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.buttonsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.buttonsLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.yourReviewsBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.yourReviewsBtn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yourReviewsBtn.sizePolicy().hasHeightForWidth())
        self.yourReviewsBtn.setSizePolicy(sizePolicy)
        self.yourReviewsBtn.setMaximumSize(QtCore.QSize(400, 50))
        self.yourReviewsBtn.setObjectName("yourReviewsBtn")
        self.buttonsLayout.addWidget(self.yourReviewsBtn)
        self.otherReviewsBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.otherReviewsBtn.setEnabled(False)
        self.otherReviewsBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.otherReviewsBtn.setObjectName("otherReviewsBtn")
        self.buttonsLayout.addWidget(self.otherReviewsBtn)
        self.paperListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.paperListWidget.setGeometry(QtCore.QRect(200, 40, 400, 230))
        self.paperListWidget.setObjectName("paperListWidget")
        self.reviewersWidget = QtWidgets.QListWidget(self.centralwidget)
        self.reviewersWidget.setGeometry(QtCore.QRect(610, 40, 400, 230))
        self.reviewersWidget.setObjectName("listWidget_2")
        self.reviewerContentWidget = QtWidgets.QTextEdit(self.centralwidget)
        self.reviewerContentWidget.setGeometry(QtCore.QRect(200, 330, 810, 330))
        self.reviewerContentWidget.setObjectName("reviewerContentWidget")
        self.reviewerContentWidget.setReadOnly(True)
        #self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        #self.listWidget_3.setGeometry(QtCore.QRect(200, 330, 810, 330))
        #self.listWidget_3.setObjectName("listWidget_3")
        self.paperListLabel = QtWidgets.QLabel(self.centralwidget)
        self.paperListLabel.setGeometry(QtCore.QRect(200, 20, 160, 20))
        self.paperListLabel.setObjectName("paperListLabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 20, 160, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 280, 80, 20))
        self.label_3.setObjectName("label_3")
        self.gradeLabel = QtWidgets.QLabel(self.centralwidget)
        self.gradeLabel.setGeometry(QtCore.QRect(290, 280, 170, 20))
        self.gradeLabel.setObjectName("gradeLabel")
        self.gradeLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.gradeLabel_2.setGeometry(QtCore.QRect(200, 310, 170, 20))
        self.gradeLabel_2.setObjectName("gradeLabel_2")
        ReviewerResults.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ReviewerResults)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        ReviewerResults.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ReviewerResults)
        self.statusbar.setObjectName("statusbar")
        ReviewerResults.setStatusBar(self.statusbar)

        self.retranslateUi(ReviewerResults)
        self.yourReviewsBtn.clicked.connect(self.openReviewerReviewsPage)
        self.yourReviewsBtn.clicked.connect(ReviewerResults.close)
        QtCore.QMetaObject.connectSlotsByName(ReviewerResults)

        paper_list = Service().reviewerPapersCheck()
        for paper in paper_list:
            item = QListWidgetItem(str(paper.paperID) + ') ' + paper.name)
            item.setData(1, paper)
            self.paperListWidget.addItem(item)


        #allReviewers = Service().reviewersListCheck()
        #for reviewer in allReviewers:
        #    reviewerItem = QListWidgetItem(str(reviewer.memberID))
        #    reviewerItem.setData(1, reviewer)
        #    self.reviewersWidget.addItem(reviewerItem)



        self.paperListWidget.itemClicked.connect(self.showReviewers)
        self.reviewersWidget.itemClicked.connect(self.showReview)
    def showReviewers(self):
        self.reviewersWidget.clear()
        allReviewers = Service().reviewersListCheck()
        for reviewer in allReviewers:
            reviewerItem = QListWidgetItem(str(reviewer.memberID))
            reviewerItem.setData(1, reviewer)
            self.reviewersWidget.addItem(reviewerItem)

    def showReview(self):
        self.reviewerContentWidget.clear()
        reviewContent = Service().reviewCheck(self.reviewersWidget.selectedIndexes()[0].data(1).memberID,
                                              self.paperListWidget.selectedIndexes()[0].data(1).paperID)
        self.reviewerContentWidget.setText(str(reviewContent.review.evaluation))
        self.gradeLabel.setText(str(reviewContent.review.result))


    def retranslateUi(self, ReviewerResults):
        _translate = QtCore.QCoreApplication.translate
        ReviewerResults.setWindowTitle(_translate("ReviewerResults", "Reviewer"))
        self.yourReviewsBtn.setText(_translate("ReviewerResults", "Your reviews"))
        self.otherReviewsBtn.setText(_translate("ReviewerResults", "Other reviews"))
        self.paperListLabel.setText(_translate("ReviewerResults", "This reviewer\'s papers"))
        self.label_2.setText(_translate("ReviewerResults", "Reviewers"))
        self.label_3.setText(_translate("ReviewerResults", "Given grade : "))
        self.gradeLabel.setText(_translate("ReviewerResults", "<selected reviewer\'s grade>"))
        self.gradeLabel_2.setText(_translate("ReviewerResults", "Selected reviewer\'s content"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReviewerResults = QtWidgets.QMainWindow()
    ui = Ui_ReviewerResults()
    ui.setupUi(ReviewerResults)
    ReviewerResults.show()
    sys.exit(app.exec_())
