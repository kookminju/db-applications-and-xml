import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("선수 테이블 검색")
        self.setGeometry(0, 0, 500, 500)

        self.label1 = QLabel("선수 검색", self)
        self.label1.move(50, 20)
        self.label2 = QLabel("팀명:", self)
        self.label2.move(80, 80)
        cb1 = QComboBox(self)
        cb1.addItem('사용안함')
        cb1.addItem('K01')
        cb1.addItem('k02')
        cb1.addItem('k03')
        cb1.addItem('k04')
        cb1.addItem('k05')
        cb1.addItem('k06')
        cb1.addItem('k07')
        cb1.addItem('k08')
        cb1.addItem('k09')
        cb1.addItem('k10')
        cb1.addItem('k11')
        cb1.addItem('k12')
        cb1.addItem('k13')
        cb1.addItem('k14')
        cb1.addItem('k15')
        cb1.move(140, 76)
        self.setGeometry(0, 0, 400, 150)
        self.label3 = QLabel("포지션:", self)
        self.label3.move(300, 80)
        cb2 = QComboBox(self)
        cb2.addItem('사용안함')
        cb2.addItem('미정')
        cb2.addItem('DF')
        cb2.addItem('FW')
        cb2.addItem('GK')
        cb2.addItem('MF')
        cb2.move(380 ,76)
        self.label4 = QLabel("출신국:", self)
        self.label4.move(540, 80)
        cb3 = QComboBox(self)
        cb3.addItem('사용안함')
        cb3.addItem('대한민국')
        cb3.addItem('김탈리아')
        cb3.addItem('나이지리아')
        cb3.addItem('러시아')
        cb3.addItem('루마니아')
        cb3.addItem('리투아니아')
        cb3.addItem('미국')
        cb3.addItem('보스니아')
        cb3.addItem('브라질')
        cb3.addItem('세네갈')
        cb3.addItem('유고')
        cb3.addItem('콜롬비아')
        cb3.addItem('크로아티아')
        cb3.move(620, 76)
        self.pushButton1 = QPushButton("초기화", self)
        self.pushButton1.move(900, 72)
        self.label5 = QLabel("키:", self)
        self.label5.move(80, 130)
        self.lineEdit1 = QLineEdit(self)
        self.lineEdit1.move(120, 126)
        self.lineEdit1.resize(100, 28)
        self.groupbox1 = QGroupBox(self)
        self.radio1 = QRadioButton("이상")
        self.radio2 = QRadioButton("이하")
        hBox = QHBoxLayout()
        hBox.addWidget(self.radio1)
        hBox.addWidget(self.radio2)
        self.groupbox1.setLayout(hBox)
        self.groupbox1.move(250, 116)
        self.label6 = QLabel("몸무게:", self)
        self.label6.move(460, 130)
        self.lineEdit2 = QLineEdit(self)
        self.lineEdit2.move(530, 126)
        self.lineEdit2.resize(100, 28)
        self.groupbox2 = QGroupBox(self)
        self.radio3 = QRadioButton("이상")
        self.radio4 = QRadioButton("이하")
        hBox = QHBoxLayout()
        hBox.addWidget(self.radio3)
        hBox.addWidget(self.radio4)
        self.groupbox2.setLayout(hBox)
        self.groupbox2.move(660, 116)
        self.pushButton2 = QPushButton("검색", self)
        self.pushButton2.move(900,122)

        self.tableWidget = QTableWidget(self)  # QTableWidget 객체 생성
        self.tableWidget.move(50, 180)
        self.tableWidget.resize(1000, 500)
        # self.tableWidget.setRowCount(len(players))  # 43
        # self.tableWidget.setColumnCount(len(players[0]))  # 13
        # columnNames = list(players[0].keys())
        # ['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'E_PLAYER_NAME', 'NICKNAME', 'JOIN_YYYY', 'POSITION', 'BACK_NO', 'NATION', 'BIRTH_DATE', 'SOLAR', 'HEIGHT', 'WEIGHT']
        # self.tableWidget.setHorizontalHeaderLabels(columnNames)
        # self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.label7 = QLabel("파일 출력", self)
        self.label7.move(50, 720)
        self.groupbox3 = QGroupBox(self)
        self.radio5 = QRadioButton("CSV")
        self.radio6 = QRadioButton("JSON")
        self.radio7 = QRadioButton("XML")
        hBox = QHBoxLayout()
        hBox.addWidget(self.radio5)
        hBox.addWidget(self.radio6)
        hBox.addWidget(self.radio7)
        self.groupbox3.setLayout(hBox)
        self.groupbox3.move(100, 760)
        self.pushButton3 = QPushButton("저장", self)
        self.pushButton3.move(900, 760)

        self.show()

    def createFirstGroup(self):
        groupbox = QGroupBox()
        self.radio1 = QRadioButton("이상")
        self.radio2 = QRadioButton("이하")

        hBox = QHBoxLayout()
        hBox.addWidget(self.radio1)
        hBox.addWidget(self.radio2)
        groupbox.setLayout(hBox)

        return groupbox

    def createSecondGroup(self):
        groupbox = QGroupBox()
        self.radio1 = QRadioButton("이상")
        self.radio2 = QRadioButton("이하")

        hBox = QHBoxLayout()
        hBox.addWidget(self.radio1)
        hBox.addWidget(self.radio2)
        groupbox.setLayout(hBox)

        return groupbox

    def createThirdGroup(self):
        groupbox = QGroupBox()
        self.radio1 = QRadioButton("CSV")
        self.radio2 = QRadioButton("JSON")
        self.radio3 = QRadioButton("XML")

        hBox = QHBoxLayout()
        hBox.addWidget(self.radio1)
        hBox.addWidget(self.radio2)
        hBox.addWidget(self.radio3)
        groupbox.setLayout(hBox)

        return groupbox

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()