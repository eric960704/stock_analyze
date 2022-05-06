import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys

class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot lib的关键
    def __init__(self, width, height, parent=None):
        fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        fig.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95)
        FigureCanvas.__init__(self, fig) # 初始化父类
        self.setParent(parent)
        self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法


    def Draw(self,ans):
        self.axes.plot(ans["日期區間"], ans["收盤價"], label = 'Price')
        self.axes.plot(ans["日期區間"], ans["損益變化"], label ='Profit')
        self.axes.grid()
        self.axes.legend()

    def Point(self,ans):
        self.axes.plot(ans["日期區間"], ans["收盤價"], label='Price')
        self.axes.grid()

        for i in range(len(ans["買賣訊號"])):
            if i == 0:
                continue
            elif ans["買賣訊號"][i-1] == -1 and ans["買賣訊號"][i] == 1:
                self.axes.annotate('buy', xy=(ans["買賣訊號"].index[i], ans["收盤價"][i]),
                                   xytext=(-50 , -50), textcoords='offset pixels',
                                   c='k', arrowprops=dict(arrowstyle = '-|>',connectionstyle="arc3,rad=.2"),
                                   bbox=dict(boxstyle='round,pad=0.5', fc='y'))
            elif ans["買賣訊號"][i-1] == 1 and ans["買賣訊號"][i] == -1:
                self.axes.annotate('sell', xy=(ans["買賣訊號"].index[i], ans["收盤價"][i]),
                                   xytext=(-50, 50), textcoords='offset pixels',
                                   c='k', arrowprops=dict(arrowstyle = '-|>',connectionstyle="arc3,rad=.2"),
                                   bbox=dict(boxstyle='round,pad=0.5', fc=(1., 0.8, 0.8)))
            elif ans["買賣訊號"][i-1] == 0 and ans["買賣訊號"][i] == 1:
                self.axes.annotate('buy', xy=(ans["買賣訊號"].index[i], ans["收盤價"][i]),
                                   xytext=(-50, -50), textcoords='offset pixels',
                                   c='k', arrowprops=dict(arrowstyle='-|>', connectionstyle="arc3,rad=.2"),
                                   bbox=dict(boxstyle='round,pad=0.5', fc='y'))
            elif ans["買賣訊號"][i-1] == 0 and ans["買賣訊號"][i] == -1:
                self.axes.annotate('sell', xy=(ans["買賣訊號"].index[i], ans["收盤價"][i]),
                                   xytext=(-50, 50), textcoords='offset pixels',
                                   c='k', arrowprops=dict(arrowstyle = '-|>',connectionstyle="arc3,rad=.2"),
                                   bbox=dict(boxstyle='round,pad=0.5', fc=(1., 0.8, 0.8)))



