import pymysql
import sys, datetime
from PyQt5.QtWidgets import *

class DB_Utils:

    def queryExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='root', password='yh691220', db=db, charset='utf8')

        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:  # dictionary based cursor
                cursor.execute(sql, params)
                tuples = cursor.fetchall()
                return tuples
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()

    def updateExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='root', password='yh691220', db=db, charset='utf8')

        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            conn.commit()
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()

class DB_Queries:
    # 모든 검색문은 여기에 각각 하나의 메소드로 정의

    def selectPlayerTeamid(self):
        sql = "SELECT DISTINCT team_id FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerUsingTeamid(self, value):
        if value == '없음':
            sql = "SELECT * FROM player WHERE team_id IS NULL"
            params = ()
        else:
            sql = "SELECT * FROM player WHERE team_id = %s"
            params = (value)  # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerPosition(self):
        sql = "SELECT DISTINCT position FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerUsingPosition(self, value):
        if value == '없음':
            sql = "SELECT * FROM player WHERE position IS NULL"
            params = ()
        else:
            sql = "SELECT * FROM player WHERE position = %s"
            params = (value)  # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerNation(self):
        sql = "SELECT DISTINCT nation FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerUsingNation(self, value):
        if value == '없음':
            sql = "SELECT * FROM player WHERE nation IS NULL"
            params = ()
        else:
            sql = "SELECT * FROM player WHERE nation = %s"
            params = (value)  # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples


# class DB_Updates:
#     # 모든 갱신문은 여기에 각각 하나의 메소드로 정의
#
#     def insertPlayer(self, player_id, player_name, team_id, position):
#         sql = "INSERT INTO player (player_id, player_name, team_id, position) VALUES (%s, %s, %s, %s)"
#         params = (player_id, player_name, team_id, position)
#
#         util = DB_Utils()
#         util.updateExecutor(db="kleague", sql=sql, params=params)


#########################################

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):

        self.setWindowTitle("선수 테이블 검색")
        self.setGeometry(0, 0, 1100, 830)

        self.label1 = QLabel("선수 검색", self)
        self.label1.move(50, 20)
        self.label2 = QLabel("팀명:", self)
        self.label2.move(80, 80)

        self.comboBox1 = QComboBox(self)
        query = DB_Queries()
        rows = query.selectPlayerTeamid()  # rows은 dictionary의 리스트
        columnName = list(rows[0].keys())[0]
        items = ['없음' if row[columnName] == None else row[columnName] for row in rows]
        self.comboBox1.addItems(items)
        self.comboBox1.move(140, 76)
        self.comboBox1.activated.connect(self.comboBox1_Activated)

        self.label3 = QLabel("포지션:", self)
        self.label3.move(300, 80)

        self.comboBox2 = QComboBox(self)
        query = DB_Queries()
        rows = query.selectPlayerPosition()  # rows은 dictionary의 리스트
        columnName = list(rows[0].keys())[0]
        items = ['없음' if row[columnName] == None else row[columnName] for row in rows]
        self.comboBox2.addItems(items)
        self.comboBox2.move(380, 76)

        self.label4 = QLabel("출신국:", self)
        self.label4.move(540, 80)

        self.comboBox3 = QComboBox(self)
        query = DB_Queries()
        rows = query.selectPlayerNation()  # rows은 dictionary의 리스트
        columnName = list(rows[0].keys())[0]
        items = ['없음' if row[columnName] == None else row[columnName] for row in rows]
        self.comboBox3.addItems(items)
        self.comboBox3.move(620, 76)

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
        self.pushButton2.clicked.connect(self.pushButton2_Clicked)

        self.tableWidget = QTableWidget(self)  # QTableWidget 객체 생성
        self.tableWidget.move(50, 180)
        self.tableWidget.resize(1000, 500)

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

    def comboBox1_Activated(self):
        self.teamidValue = self.comboBox1.currentText()  # positionValue를 통해 선택한 포지션 값을 전달

    def comboBox2_Activated(self):
        self.positionValue = self.comboBox2.currentText()

    def comboBox3_Activated(self):
        self.nationValue = self.comboBox3.currentText()

    def pushButton2_Clicked(self):

        # DB 검색문 실행
        query = DB_Queries()
        players = query.selectPlayerUsingPosition(self.teamidValue)

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(players))
        self.tableWidget.setColumnCount(len(players[0]))
        columnNames = list(players[0].keys())
        self.tableWidget.setHorizontalHeaderLabels(columnNames)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for rowIDX in range(len(players)):
            player = players[rowIDX]

            for k, v in player.items():
                columnIDX = columnNames.index(k)

                if v == None:           # 파이썬이 DB의 널값을 None으로 변환함.
                    continue            # QTableWidgetItem 객체를 생성하지 않음
                elif isinstance(v, datetime.date):      # QTableWidgetItem 객체 생성
                    item = QTableWidgetItem(v.strftime('%Y-%m-%d'))
                else:
                    item = QTableWidgetItem(str(v))

                self.tableWidget.setItem(rowIDX, columnIDX, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

main()