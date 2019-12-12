from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
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
        self.comboSubject.addItems(['소프트웨어프로젝트2', '창업연계공학설계입문', '객체지향프로그램', '선형대수'])
        self.comboClass.addItems(['class1', 'class2', 'class3'])
        self.comboClass.currentTextChanged.connect(self.comboClicked)
        self.comboSubject.currentTextChanged.connect(self.comboClicked)

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

        self.checkClass = QCheckBox("분반 별 그래프 보기")
        font = self.checkClass.font()
        font.setPointSize(font.pointSize() + 3)
        self.checkClass.setFont(font)
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
        funcLayout.addWidget(self.checkClass)
        funcLayout.addSpacing(10)
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


    # clicked btnInputScore
    def btnInputScoreClicked(self):
        file = open("scoreDB.txt", 'w')




    def comboClicked(self):
        self.txtGraphTitle = QLabel("< " + self.comboSubject.currentText() + " > - " +
                                self.comboClass.currentText() + " graph")


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
        ax.legend()     # 범례 표시

        self.canvas.draw()




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())




