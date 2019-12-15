from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from InputDialog import InputDialog
import pickle
import os


class Main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.class1_SW_score = []
        self.class1_LA_score = []
        self.class2_SW_score = []
        self.class2_LA_score = []
        self.setData()
        self.initUI()
        self.drawGraph()

    def initUI(self):
        self.setWindowTitle("성적산출프로그램")
        self.setGeometry(650, 200, 750, 550)
        self.lblSubject = QLabel("과목 선택하기")
        font = self.lblSubject.font()
        font.setPointSize(font.pointSize() + 5)
        self.lblSubject.setFont(font)
        self.lblSubject.setFixedSize(150, 20)       # fixed widget size
        self.comboSubject = QComboBox()
        self.comboSubject.setFixedSize(150, 30)
        self.lblClass = QLabel("분반 선택하기")
        font = self.lblClass.font()
        font.setPointSize(font.pointSize() + 5)
        self.lblClass.setFont(font)
        self.comboClass = QComboBox()
        self.comboClass.setFixedSize(80, 30)
        self.comboSubject.addItems(['소프트웨어프로젝트2', '선형대수'])
        self.comboClass.addItems(['class1', 'class2'])
        # self.comboClass.currentTextChanged.connect(self.comboClicked)
        # self.comboSubject.currentTextChanged.connect(self.comboClicked)

        self.btnInputScore = QPushButton("점수 입력하기")
        self.btnInputScore.clicked.connect(self.btnInputScoreClicked)
        self.btnReset = QPushButton("점수 초기화")
        font = self.btnInputScore.font()
        font.setPointSize(font.pointSize() + 3)
        self.btnInputScore.setFont(font)
        self.btnInputScore.setFixedSize(200, 40)

        font = self.btnReset.font()
        font.setPointSize(font.pointSize() + 3)
        self.btnReset.setFont(font)
        self.btnReset.setFixedSize(200, 40)

        # self.checkClass = QCheckBox("분반 별 그래프 보기")
        # font = self.checkClass.font()
        # font.setPointSize(font.pointSize() + 3)
        # self.checkClass.setFont(font)
        self.checkAll =  QCheckBox("모든 분반 그래프 보기")
        font = self.checkAll.font()
        font.setPointSize(font.pointSize() + 3)
        self.checkAll.setFont(font)

        funcLayout = QVBoxLayout()
        funcLayout.addWidget(self.lblSubject)
        funcLayout.addSpacing(13)
        funcLayout.addWidget(self.comboSubject)
        funcLayout.addSpacing(15)
        funcLayout.addWidget(self.lblClass)
        funcLayout.addSpacing(13)
        funcLayout.addWidget(self.comboClass)
        funcLayout.addSpacing(65)
        funcLayout.addWidget(self.btnInputScore)
        funcLayout.addSpacing(10)
        funcLayout.addWidget(self.btnReset)
        funcLayout.addSpacing(60)
        # funcLayout.addWidget(self.checkClass)
        # funcLayout.addSpacing(10)
        funcLayout.addWidget(self.checkAll)
        funcLayout.setContentsMargins(20, 50, 0, 50)    # layout margins(left, top, right, bottom)

        #graph
        self.txtGraphTitle = QLabel("< " + self.comboSubject.currentText() + " > - " +
                                    self.comboClass.currentText() + " graph")
        font = self.txtGraphTitle.font()
        font.setPointSize(font.pointSize() + 3)
        self.txtGraphTitle.setFont(font)
        self.txtGraphTitle.setAlignment(Qt.AlignCenter)
        self.scores = [x for x in range(0, 100, 10)]
        self.people = [x for x in range(0, 12, 2)]
        self.fig = plt.Figure()
        self.fig.set_size_inches(4.5, 4.5)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xticks(self.scores)
        self.ax.set_yticks(self.people)
        self.canvas = FigureCanvas(self.fig)

        self.lblAverage = QLabel("평균 : ")
        font = self.lblAverage.font()
        font.setPointSize(font.pointSize() + 3)
        self.lblAverage.setFont(font)
        self.lblVariance = QLabel("분산 : ")
        font = self.lblVariance.font()
        font.setPointSize(font.pointSize() + 3)
        self.lblVariance.setFont(font)
        self.txtAverage = QLabel()
        self.txtVariance = QLabel()

        graphLayout = QVBoxLayout()
        graphLayout.addWidget(self.txtGraphTitle)
        graphLayout.addSpacing(10)
        graphLayout.addWidget(self.canvas)
        graphLayout.addSpacing(40)

        resultLayout = QHBoxLayout()
        resultLayout.addWidget(self.lblAverage)
        resultLayout.addWidget(self.txtAverage)
        resultLayout.addWidget(self.lblVariance)
        resultLayout.addWidget(self.txtVariance)
        resultLayout.setContentsMargins(50, 0, 0, 0)
        graphLayout.addLayout(resultLayout)
        graphLayout.setContentsMargins(0, 30, 20, 50)

        mainLayout = QGridLayout()
        mainLayout.addLayout(funcLayout,0, 0)
        mainLayout.addLayout(graphLayout,0, 1)

        self.setLayout(mainLayout)


    # Subject comboBox의 key값 리턴
    def getSubKey(self):
        return self.comboSubject.currentText()

    # Class comboBox의 key값 리턴
    def getClassKey(self):
        return self.comboClass.currentText()

    # clicked btnInputScore -> dialog
    def btnInputScoreClicked(self):
        self.data = []
        self.setScore()
        self.dlg = InputDialog(self.data)   # 매개변수 self.data : dialog에 입력했던 점수를 불러오기 위한 장치
        self.dlg.exec_()
        self.dumpData()
        self.setData()


    # 다이얼로그 창에서 받아온 점수리스트를 comboBox의 키 값에 따라 각각의 리스트에 점수 저장 & 텍스트파일에 값 저장
    def dumpData(self):
        n = self.dlg.btnOkClicked()     # dialog에 입력한 점수 리스트
        if self.getSubKey() == "소프트웨어프로젝트2" and self.getClassKey() == "class1":
            file = open('class1_SW_scoreDB.txt', 'wb')
            pickle.dump(n, file)

        elif self.getSubKey() == "선형대수" and self.getClassKey() == "class1":
            file = open('class1_LA_scoreDB.txt', 'wb')
            pickle.dump(n, file)

        elif self.getSubKey() == "소프트웨어프로젝트2" and self.getClassKey() == "class2":
            file = open('class2_SW_scoreDB.txt', 'wb')
            pickle.dump(n, file)

        elif self.getSubKey() == "선형대수" and self.getClassKey() == "class2":
            file = open('class2_LA_scoreDB.txt', 'wb')
            pickle.dump(n, file)


    # 텍스트파일에 저장되어있는 점수 불러오기
    def setData(self):
        if os.path.getsize('class1_SW_scoreDB.txt') > 0:
            file = open('class1_SW_scoreDB.txt', 'rb')
            self.class1_SW_score = pickle.load(file)
        else:
            pass

        if os.path.getsize('class1_LA_scoreDB.txt') > 0:
            file = open('class1_LA_scoreDB.txt', 'rb')
            self.class1_LA_score = pickle.load(file)
        else:
            pass

        if os.path.getsize('class2_SW_scoreDB.txt') > 0:
            file = open('class2_SW_scoreDB.txt', 'rb')
            self.class2_SW_score = pickle.load(file)
        else:
            pass


        if os.path.getsize('class2_LA_scoreDB.txt') > 0:
            file = open('class2_LA_scoreDB.txt', 'rb')
            self.class2_LA_score = pickle.load(file)
        else:
            pass

    # 각각의 파일에서 점수를 가져와서 다이얼로그 lineEdit에 점수 저장
    def setScore(self):
        if self.getSubKey() == "소프트웨어프로젝트2" and self.getClassKey() == "class1":
            if os.path.getsize('class1_SW_scoreDB.txt') > 0:
                file = open('class1_SW_scoreDB.txt', 'rb')
                self.data =  pickle.load(file)
            else:
                self.data = []

        elif self.getSubKey() == "선형대수" and self.getClassKey() == "class1":
            if os.path.getsize('class1_LA_scoreDB.txt') > 0:
                file = open('class1_LA_scoreDB.txt', 'rb')
                self.data =  pickle.load(file)
            else:
                self.data = []

        elif self.getSubKey() == "소프트웨어프로젝트2" and self.getClassKey() == "class2":
            if os.path.getsize('class2_SW_scoreDB.txt') > 0:
                file = open('class2_SW_scoreDB.txt', 'rb')
                self.data =  pickle.load(file)
            else:
                self.data = []

        elif self.getSubKey() == "선형대수" and self.getClassKey() == "class2":
            if os.path.getsize('class2_LA_scoreDB.txt') > 0:
                file = open('class2_LA_scoreDB.txt', 'rb')
                self.data =  pickle.load(file)
            else:
                self.data = []



    def drawGraph(self):

        x = [90, 80, 70, 60, 40]
        y = [2, 4, 6, 0, 2]

        x1 = [90, 80, 70, 60, 40]
        y1 = [4, 8, 2, 6, 1]

        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.set_xticks(self.scores)
        ax.set_yticks(self.people)
        ax.plot(x, y, label="class1", marker='o')
        ax.plot(x1, y1, label="class2", marker='o')
        ax.legend()  # 범례 표시

        self.canvas.draw()




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())




