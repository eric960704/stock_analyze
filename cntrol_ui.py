import sys,MA,KD,RSI,MACD,bolling,traceback,time
import Graphics as graph
from PyQt5.QtGui import QPixmap ,QPainter
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from main import Ui_MainWindow  # 取得主介面
from prediction import Ui_prediction  # 取得預測介面
from Backtest import Ui_backtest  # 取得回測界面
from descripe import Ui_descripetion    #取得描述介面
import PriceGraphic
from PyQt5.QtWidgets import QMainWindow
import pyqtgraph as pg
import recommend
from PyQt5 import QtCore

# 主介面
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.prediction_ui_btn.clicked.connect(self.Pre_ShowUi)
        self.backtest_ui_Btn.clicked.connect(self.Back_ShowUi)
        self.descripe_ui_btn.clicked.connect(self.Descripe_ShowUi)

    # 點選buttton跳至預測系統
    def Pre_ShowUi(self):
        self.pre_ui = Prediction_Ui()
        self.pre_ui.show()

    # 點選buttton跳至回測系統
    def Back_ShowUi(self):
        self.back_ui = Backtest_Ui()
        self.back_ui.show()

    # 點選buttton跳至介紹
    def Descripe_ShowUi(self):
        self.Descripe_ui = Descripe_ui()
        self.Descripe_ui.show()

    # 預測系統介面
class Prediction_Ui(QWidget, Ui_prediction):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exitButton.clicked.connect(self.close)
        self.buyButton1.hide()
        self.buyButton2.hide()
        self.buyButton3.hide()
        self.buyButton4.hide()
        self.buyButton5.hide()
        self.buyButton6.hide()
        self.buyButton7.hide()
        self.buyButton8.hide()
        self.buyButton9.hide()
        self.buyButton10.hide()
        self.buyButton11.hide()
        self.buyButton12.hide()
        self.sellButton1.hide()
        self.sellButton2.hide()
        self.sellButton3.hide()
        self.sellButton4.hide()
        self.sellButton5.hide()
        self.sellButton6.hide()
        self.sellButton7.hide()
        self.sellButton8.hide()
        self.sellButton9.hide()
        self.sellButton10.hide()
        self.sellButton11.hide()
        self.sellButton12.hide()
        date = MACD.Date
        self.prediction_date.setText("日期 :"+date.strftime("%Y/%m/%d"))
        self.show_recommend()

    # 推薦使用者股票
    def show_recommend(self):
        _translate = QtCore.QCoreApplication.translate
        recommend_total = recommend.total  # 字典 EX:{2330,1 ...}
        buy_times = 1
        sell_times = 1
        for item in recommend_total.items():
            if (item[1] == 1):
                if buy_times == 1:
                    self.buyButton1.setText(_translate("prediction", item[0]))
                    self.buyButton1.show()
                    buy_times += 1
                elif buy_times == 2:
                    self.buyButton2.setText(_translate("prediction", item[0]))
                    self.buyButton2.show()
                    buy_times += 1
                elif buy_times == 3:
                    self.buyButton3.setText(_translate("prediction", item[0]))
                    self.buyButton3.show()
                    buy_times += 1
                elif buy_times == 4:
                    self.buyButton4.setText(_translate("prediction", item[0]))
                    self.buyButton4.show()
                    buy_times += 1
                elif buy_times == 5:
                    self.buyButton5.setText(_translate("prediction", item[0]))
                    self.buyButton5.show()
                    buy_times += 1
                elif buy_times == 6:
                    self.buyButton6.setText(_translate("prediction", item[0]))
                    self.buyButton6.show()
                    buy_times += 1
                elif buy_times == 7:
                    self.buyButton7.setText(_translate("prediction", item[0]))
                    self.buyButton7.show()
                    buy_times += 1
                elif buy_times == 8:
                    self.buyButton8.setText(_translate("prediction", item[0]))
                    self.buyButton8.show()
                    buy_times += 1
                elif buy_times == 9:
                    self.buyButton9.setText(_translate("prediction", item[0]))
                    self.buyButton9.show()
                    buy_times += 1
                elif buy_times == 10:
                    self.buyButton10.setText(_translate("prediction", item[0]))
                    self.buyButton10.show()
                    buy_times += 1
                elif buy_times == 11:
                    self.buyButton11.setText(_translate("prediction", item[0]))
                    self.buyButton11.show()
                    buy_times += 1
                elif buy_times == 12:
                    self.buyButton12.setText(_translate("prediction", item[0]))
                    self.buyButton12.show()
                    buy_times += 1

            elif (item[1] == -1):
                if sell_times == 1:
                    self.sellButton1.setText(_translate("prediction", item[0]))
                    self.sellButton1.show()
                    sell_times += 1
                elif sell_times == 2:
                    self.sellButton2.setText(_translate("prediction", item[0]))
                    self.sellButton2.show()
                    sell_times += 1
                elif sell_times == 3:
                    self.sellButton3.setText(_translate("prediction", item[0]))
                    self.sellButton3.show()
                    sell_times += 1
                elif sell_times == 4:
                    self.sellButton4.setText(_translate("prediction", item[0]))
                    self.sellButton4.show()
                    sell_times += 1
                elif sell_times == 5:
                    self.sellButton5.setText(_translate("prediction", item[0]))
                    self.sellButton5.show()
                    sell_times += 1
                elif sell_times == 6:
                    self.sellButton6.setText(_translate("prediction", item[0]))
                    self.sellButton6.show()
                    sell_times += 1
                elif sell_times == 7:
                    self.sellButton7.setText(_translate("prediction", item[0]))
                    self.sellButton7.show()
                    sell_times += 1
                elif sell_times == 8:
                    self.sellButton8.setText(_translate("prediction", item[0]))
                    self.sellButton8.show()
                    sell_times += 1
                elif sell_times == 9:
                    self.sellButton9.setText(_translate("prediction", item[0]))
                    self.sellButton9.show()
                    sell_times += 1
                elif sell_times == 10:
                    self.sellButton10.setText(_translate("prediction", item[0]))
                    self.sellButton10.show()
                    sell_times += 1
                elif sell_times == 11:
                    self.sellButton11.setText(_translate("prediction", item[0]))
                    self.sellButton11.show()
                    sell_times += 1
                elif sell_times == 12:
                    self.sellButton12.setText(_translate("prediction", item[0]))
                    self.sellButton12.show()
                    sell_times += 1


    # 設置背景和顏色
    def paintEvent(self, event):
        painter = QPainter(self)
        # 設置背景颜色
        # painter.setBrush(Qt.green)
        # painter.drawRect(self.rect())
        # 設置背景图片，平铺到整个窗口，随着窗口改变而改变
        pixmap = QPixmap(r"C:\Users\as298\PycharmProjects\stock_ui\backup.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    # 回測系統介面
class Backtest_Ui(QWidget, Ui_backtest):
    ans = None
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_back.clicked.connect(self.backtest)    #開始回測
        self.Strategy.currentIndexChanged[str].connect(self.Detect_signal)  #欄位會隨策略變化
        self.PriceGraph_Button.clicked.connect(self.PriceGraph_Btn_Clicked)    #損益圖
        self.PricePoint_btn.clicked.connect(self.PricePoint_btn_Clicked)  # 進出場點位圖
        self.close_button.clicked.connect(self.close)   #離開
        self.graphicsView.hide()    #先隱藏損益圖
        self.k_widget = QtWidgets.QWidget()  # 实例化一个widget部件作为K线图部件
        self.k_layout = QtWidgets.QGridLayout()  # 实例化一个网格布局层
        self.k_widget.setLayout(self.k_layout)  # 设置K线图部件的布局层
        self.k_plt = pg.PlotWidget()  # 实例化一个绘图部件
        self.k_layout.addWidget(self.k_plt)     #圖片放到layout
        self.gridLayout_2.addWidget(self.k_widget, 1, 0, 3, 3)  #layout放到grid


    # 偵測策略的method
    def Detect_signal(self, signal):
        if signal == "Boiling(布林通道)":
            self.all_show()
            self.LongMaText.hide()
            self.tall_ma_low.hide()
            self.tall_ma_high.hide()
            self.tilde2.hide()
            self.ShortMaText.setText("均線")
        elif signal == "MA(均線)":
            self.all_show()
            self.ShortMaText.setText("短均線")
            self.LongMaText.setText("長均線")
        elif signal == "MACD(指數平滑異同移動平均線)":
            self.all_show()
            self.ShortMaText.setText("短均線")
            self.LongMaText.setText("長均線")
        elif signal == "KD(隨機指標)":
            self.all_show()
            self.ShortMaText.setText("KD>")
            self.LongMaText.setText("KD<")
        elif signal == "RSI(相對強弱指標)":
            self.all_show()
            self.ShortMaText.setText("短RSI")
            self.LongMaText.setText("長RSI")
            self.tilde2.show()
        else:
            self.all_show()

    # 偵測策略的method全部顯示
    def all_show(self):
        self.tall_ma_low.show()
        self.tilde2.show()
        self.tall_ma_high.show()
        self.LongMaText.show()

    # 繪製K線
    def Graphical_query_slot(self):
        try:
            self.start_back.setEnabled(False)
            self.start_back.setText("回測中…")
            code = self.stock_number.text()
            start_date_str = self.frontDate.text()
            end_date_str = self.backDate.text()
            graph.plot_k_line(self, code=code, start=start_date_str, end=end_date_str)
            self.graphicsView.hide()
            self.k_widget.show()
            self.start_back.setEnabled(True)
            self.start_back.setText("開始回測")
        except Exception as e:
            print(traceback.print_exc())

    #繪製收盤價與損益圖
    def PriceGraph_Btn_Clicked(self):
        if self.ans != None:
            if self.graphicsView.isHidden():
                # 方法在PriceGraphic.py
                Canvas_1 = PriceGraphic.Figure_Canvas(13.8,6.4)
                Canvas_1.Draw(self.ans)
                self.graphicscene1 = QtWidgets.QGraphicsScene()
                self.graphicscene1.addWidget(Canvas_1)
                self.graphicsView.setScene(self.graphicscene1)
                self.k_widget.hide()
                self.graphicsView.show()
            else :
                self.graphicsView.hide()
                self.k_widget.show()
        else:
            self.back_ans.setText("沒有回測資料")

    # 繪製進出場點
    def PricePoint_btn_Clicked(self):
        if self.ans != None:
            if self.graphicsView.isHidden():
                # 方法在PriceGraphic.py
                Canvas_2 = PriceGraphic.Figure_Canvas(100,6.2)
                Canvas_2.Point(self.ans)
                self.graphicscene2 = QtWidgets.QGraphicsScene()
                self.graphicscene2.addWidget(Canvas_2)
                self.graphicsView.setScene(self.graphicscene2)
                self.k_widget.hide()
                self.graphicsView.show()
            else :
                self.graphicsView.hide()
                self.k_widget.show()
        else:
            self.back_ans.setText("沒有回測資料")

    # 回測功能
    def backtest(self):
        starategy = self.Strategy.currentText()
        stock_number = self.stock_number.text()
        # 轉換時間格式
        toDate = time.strptime(self.frontDate.text(), "%Y/%m/%d")
        frontDate = time.strftime("%Y-%m-%d", toDate)
        toDate2 = time.strptime(self.backDate.text(), "%Y/%m/%d")
        backDate = time.strftime("%Y-%m-%d", toDate2)

        print(starategy)
        print(stock_number)
        print(frontDate, backDate)

        if stock_number != "":
            if starategy == "MA(均線)":
                ShortMa_min = self.shart_ma_low.text()
                ShortMa_max = self.shart_ma_high.text()
                LongMa_min = self.tall_ma_low.text()
                LongMa_max = self.tall_ma_high.text()
                if ShortMa_min != "" and ShortMa_max != "" and LongMa_min != "" and LongMa_max != "":  # 資料不能為空值
                    self.ans = MA.simple_back_ma(int(stock_number), int(ShortMa_min), int(ShortMa_max), int(LongMa_min),
                                            int(LongMa_max), frontDate, backDate)  # 傳入股票代號
                    if self.ans != None:  # 不為空就印出
                        self.Graphical_query_slot()  #畫K線圖
                        self.back_ans.setText("代碼 : " + str(self.ans["代碼"]) + "\n" +
                                              "回測日期 : " + str(self.ans["日期區間"][0]) + " ~ " +
                                              str(self.ans["日期區間"][-1]) + "\n" +
                                              "策略損益 : " + str(self.ans["最佳損益"]) + "\n" +
                                              "股票漲幅 : " + str(self.ans["股票漲幅"]) + "\n" +
                                              "最佳短均線 : " + str(self.ans["最佳短均線"]) + "\n" +
                                              "最佳長均線 : " + str(self.ans["最佳長均線"]) + "\n" +
                                              "交易次數 : " + str(self.ans["交易次數"]) + "\n" +
                                              "獲利次數 : " + str(self.ans["獲利次數"]) + "\n" +
                                              "虧損次數 : " + str(self.ans["虧損次數"]) + "\n" +
                                              "平均每次交易損益 : " + str(self.ans["平均每次交易損益"]) + "\n" +
                                              "平均每次交易勝率 : " + str(self.ans["平均每次交易勝率"]) + "\n" +
                                              "單次最大獲利 : " + str(self.ans["單次最大獲利"]) + "\n" +
                                              "單次最大虧損 : " + str(self.ans["單次最大虧損"]) + "\n"
                                              )
                    else:
                        self.back_ans.setText("沒有交易或沒有股票代號")
                else:
                    self.back_ans.setText("沒設置參數")

            elif starategy == "KD(隨機指標)":
                MaxKDUp = self.shart_ma_low.text()
                MaxKDLower = self.shart_ma_high.text()
                MinKDUp = self.tall_ma_low.text()
                MinKDLower = self.tall_ma_high.text()
                if MaxKDUp != "" and MaxKDLower != "" and MinKDUp != "" and MinKDLower != "":
                    self.ans = KD.simple_back_KD(int(stock_number), int(MaxKDUp), int(MaxKDLower), int(MinKDUp),
                                            int(MinKDLower), frontDate, backDate)
                    if self.ans != None:  # 不為空就印出
                        self.Graphical_query_slot()  # 畫K線圖
                        self.back_ans.setText("代碼 : " + str(self.ans["代碼"]) + "\n" +
                                              "回測日期 : " + str(self.ans["日期區間"][0]) + " ~ " +
                                              str(self.ans["日期區間"][-1]) + "\n" +
                                              "策略損益 :" + str(self.ans["最佳損益"]) + "\n" +
                                              "股票漲幅 :" + str(self.ans["股票漲幅"]) + "\n" +
                                              "最佳KD值買 :" + str(self.ans["最佳KD值買"]) + "\n" +
                                              "最佳KD值賣 :" + str(self.ans["最佳KD值賣"]) + "\n" +
                                              "交易次數 :" + str(self.ans["交易次數"]) + "\n" +
                                              "獲利次數 :" + str(self.ans["獲利次數"]) + "\n" +
                                              "虧損次數 :" + str(self.ans["虧損次數"]) + "\n" +
                                              "平均每次交易損益 :" + str(self.ans["平均每次交易損益"]) + "\n" +
                                              "平均每次交易勝率 :" + str(self.ans["平均每次交易勝率"]) + "\n" +
                                              "單次最大獲利 :" + str(self.ans["單次最大獲利"]) + "\n" +
                                              "單次最大虧損 :" + str(self.ans["單次最大虧損"]) + "\n"
                                              )
                    else:
                        self.back_ans.setText("沒有交易或沒有股票代號")
                else:
                    self.back_ans.setText("沒設置參數")

            elif starategy == "RSI(相對強弱指標)":
                RsiLower1 = self.shart_ma_low.text()
                RsiLower2 = self.shart_ma_high.text()
                RsiUper1 = self.tall_ma_low.text()
                RsiUper2 = self.tall_ma_high.text()
                if RsiLower1 != "" and RsiLower2 != "" and RsiUper1 != "" and RsiUper2 != "":
                    self.ans = RSI.simple_back_RSI(int(stock_number), int(RsiLower1), int(RsiLower2), int(RsiUper1),
                                              int(RsiUper2), frontDate, backDate)
                    if self.ans != None:  # 不為空就印出
                        self.Graphical_query_slot()  # 畫K線圖
                        self.back_ans.setText("代碼 : " + str(self.ans["代碼"]) + "\n" +
                                              "回測日期 : " + str(self.ans["日期區間"][0]) + " ~ " +
                                              str(self.ans["日期區間"][-1]) + "\n" +
                                              "策略損益 :" + str(self.ans["最佳損益"]) + "\n" +
                                              "股票漲幅 :" + str(self.ans["股票漲幅"]) + "\n" +
                                              "最佳短RSI :" + str(self.ans["最佳短RSI"]) + "\n" +
                                              "最佳長RSI :" + str(self.ans["最佳長RSI"]) + "\n" +
                                              "交易次數 :" + str(self.ans["交易次數"]) + "\n" +
                                              "獲利次數 :" + str(self.ans["獲利次數"]) + "\n" +
                                              "虧損次數 :" + str(self.ans["虧損次數"]) + "\n" +
                                              "平均每次交易損益 :" + str(self.ans["平均每次交易損益"]) + "\n" +
                                              "平均每次交易勝率 :" + str(self.ans["平均每次交易勝率"]) + "\n" +
                                              "單次最大獲利 :" + str(self.ans["單次最大獲利"]) + "\n" +
                                              "單次最大虧損 :" + str(self.ans["單次最大虧損"]) + "\n"
                                              )
                    else:
                        self.back_ans.setText("沒有交易或沒有股票代號")
                else:
                    self.back_ans.setText("沒設置參數")

            elif starategy == "MACD(指數平滑異同移動平均線)":
                ShortMa_min = self.shart_ma_low.text()
                ShortMa_max = self.shart_ma_high.text()
                LongMa_min = self.tall_ma_low.text()
                LongMa_max = self.tall_ma_high.text()
                if ShortMa_min != "" and ShortMa_max != "" and LongMa_min != "" and LongMa_max != "":  # 資料不能為空值
                    self.ans = MACD.simple_back_MACD(int(stock_number), int(ShortMa_min), int(ShortMa_max), int(LongMa_min),
                                                int(LongMa_max), frontDate, backDate)  # 傳入股票代號
                    if self.ans != None:  # 不為空就印出
                        self.Graphical_query_slot()  # 畫K線圖
                        self.back_ans.setText("代碼 : " + str(self.ans["代碼"]) + "\n" +
                                              "回測日期 : " + str(self.ans["日期區間"][0]) + " ~ " +
                                              str(self.ans["日期區間"][-1]) + "\n" +
                                              "策略損益 :" + str(self.ans["最佳損益"]) + "\n" +
                                              "股票漲幅 :" + str(self.ans["股票漲幅"]) + "\n" +
                                              "最佳短均線 :" + str(self.ans["最佳短均線"]) + "\n" +
                                              "最佳長均線 :" + str(self.ans["最佳長均線"]) + "\n" +
                                              "交易次數 :" + str(self.ans["交易次數"]) + "\n" +
                                              "獲利次數 :" + str(self.ans["獲利次數"]) + "\n" +
                                              "虧損次數 :" + str(self.ans["虧損次數"]) + "\n" +
                                              "平均每次交易損益 :" + str(self.ans["平均每次交易損益"]) + "\n" +
                                              "平均每次交易勝率 :" + str(self.ans["平均每次交易勝率"]) + "\n" +
                                              "單次最大獲利 :" + str(self.ans["單次最大獲利"]) + "\n" +
                                              "單次最大虧損 :" + str(self.ans["單次最大虧損"]) + "\n"
                                              )
                    else:
                        self.back_ans.setText("沒有交易或沒有股票代號")
                else:
                    self.back_ans.setText("沒設置參數")

            elif starategy == "Boiling(布林通道)":
                ShortMa_min = self.shart_ma_low.text()
                ShortMa_max = self.shart_ma_high.text()
                if ShortMa_min != "" and ShortMa_max != "":  # 資料不能為空值
                    self.ans = bolling.simple_back_boiling(int(stock_number), int(ShortMa_min), int(ShortMa_max)
                                                      , frontDate, backDate)  # 傳入股票代號
                    if self.ans != None:  # 不為空就印出
                        self.Graphical_query_slot()  # 畫K線圖
                        self.back_ans.setText("代碼 : " + str(self.ans["代碼"]) + "\n" +
                                              "回測日期 : " + str(self.ans["日期區間"][0]) + " ~ " +
                                              str(self.ans["日期區間"][-1]) + "\n" +
                                              "策略損益 :" + str(self.ans["最佳損益"]) + "\n" +
                                              "股票漲幅 :" + str(self.ans["股票漲幅"]) + "\n" +
                                              "最佳布林均線 :" + str(self.ans["最佳布林均線"]) + "\n" +
                                              "交易次數 :" + str(self.ans["交易次數"]) + "\n" +
                                              "獲利次數 :" + str(self.ans["獲利次數"]) + "\n" +
                                              "虧損次數 :" + str(self.ans["虧損次數"]) + "\n" +
                                              "平均每次交易損益 :" + str(self.ans["平均每次交易損益"]) + "\n" +
                                              "平均每次交易勝率 :" + str(self.ans["平均每次交易勝率"]) + "\n" +
                                              "單次最大獲利 :" + str(self.ans["單次最大獲利"]) + "\n" +
                                              "單次最大虧損 :" + str(self.ans["單次最大虧損"]) + "\n"
                                              )
                    else:
                        self.back_ans.setText("沒有交易或沒有股票代號")
                else:
                    self.back_ans.setText("沒設置參數")
            else:
                self.back_ans.setText("未選擇策略")
        else:
            self.back_ans.setText("未設置股票代號")

    def print_slot(self, event=None):
        if event is None:
            print("事件為空")
        else:
            pos = event[0]  # 获取事件的鼠标位置
            try:
                # 如果鼠标位置在绘图部件中
                if self.k_plt.sceneBoundingRect().contains(pos):
                    mousePoint = self.k_plt.plotItem.vb.mapSceneToView(pos)  # 转换鼠标坐标
                    index = int(mousePoint.x())  # 鼠标所处的X轴坐标
                    pos_y = int(mousePoint.y())  # 鼠标所处的Y轴坐标
                    if -1 < index < len(self.data.index):
                        # 在label中写入HTML
                        self.label.setHtml(
                            "<p style='color:white'><strong>日期：{0}</strong></p><p style='color:white'>開盤：{1}</p><p style='color:white'>收盤：{2}</p><p style='color:white'>最高：<span style='color:red;'>{3}</span></p><p style='color:white'>最低：<span style='color:green;'>{4}</span></p>".format(
                                self.axis_dict[index], self.data['Open'][index], self.data['Close'][index],
                                self.data['High'][index], self.data['Low'][index]))
                        self.label.setPos(mousePoint.x(), mousePoint.y())  # 设置label的位置
                    # 设置垂直线条和水平线条的位置组成十字光标
                    self.vLine.setPos(mousePoint.x())
                    self.hLine.setPos(mousePoint.y())
            except Exception as e:
                print(traceback.print_exc())

    #介紹介面
class Descripe_ui(QWidget, Ui_descripetion):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
