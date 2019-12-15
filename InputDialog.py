from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class InputDialog(QDialog):
    def __init__(self, score_lst):
        super().__init__()
        self.setupUI(score_lst)



    def setupUI(self, score_lst):
        self.setGeometry(650, 300, 600, 400)
        self.setWindowTitle("점수 입력하기")

        self.lblMessage = QLabel("각각의 빈 칸에 학생들의 점수를 입력하세요.")
        font = self.lblMessage.font()
        font.setPointSize(font.pointSize() + 3)
        self.lblMessage.setFont(font)

        grid1 = QGridLayout()
        grid1.addWidget(self.lblMessage)

        grid2 = QGridLayout()
        r = 0; c = 0

        # lineEdit widget배치
        self.line_lst = []
        for i in range(20):
            lineEdit = QLineEdit()
            lineEdit.setFixedSize(100, 30)
            self.line_lst.append(lineEdit)
            grid2.addWidget(lineEdit, r, c)
            r += 1
            if r > 4:
                r = 0
                c += 1
        for i in range(len(self.line_lst)):
            if len(score_lst) != 0 and score_lst[i] != 0:
                self.line_lst[i].setText(str(score_lst[i]))


        main = QGridLayout()
        main.addLayout(grid1, 0, 0)
        main.addLayout(grid2, 1, 0)

        self.btnOk = QPushButton("확인")
        self.btnOk.setFixedSize(100, 30)
        self.btnOk.clicked.connect(self.btnOkClicked)

        main.addWidget(self.btnOk, 2, 3)
        self.setLayout(main)

    # 확인 버튼을 클릭 -> line_lst의 LineEdit객체를 가져와서 예외 처리, score리스트를 메인 윈도우에 보내기 위해 리턴
    def btnOkClicked(self):
        self.score = []
        for i in range(len(self.line_lst)):
            try:
                n = int(self.line_lst[i].text())
            except:
                n = 0
            self.score.append(n)

        self.close()
        return self.score




