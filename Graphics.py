import PyQt5
import pyqtgraph as pg
import MA as Ma
from datetime import datetime
import traceback


def plot_k_line(self, code=None, start=None, end=None):

    start = datetime.strptime(start, "%Y/%m/%d").date()
    end = datetime.strptime(end, "%Y/%m/%d").date()
    self.data = Ma.stock.loc[(Ma.stock.Id == int(code))]
    self.data = self.data.set_index('Date')
    self.data = self.data[start:end]
    self.data = self.data.drop('Id', axis=1)
    y_min = self.data['Low'].min()
    y_max = self.data['High'].max()
    data_list = []
    d = 0
    for dates, row in self.data.iterrows():
        Open, High, Low, Close = row[:4]
        datas = (d, Open, Close, Low, High)
        data_list.append(datas)
        d += 1
    self.axis_dict = dict(enumerate(self.data.index))
    axis_1 = [(i, list(self.data.index)[i]) for i in range(0, len(self.data.index), 1)]  # 获取日期值
    axis_2 = [(i, list(self.data.index)[i]) for i in range(0, len(self.data.index), 5)]
    axis_3 = [(i, list(self.data.index)[i]) for i in range(0, len(self.data.index), 10)]
    axis_4 = [(i, list(self.data.index)[i]) for i in range(0, len(self.data.index), 20)]
    axis_5 = [(i, list(self.data.index)[i]) for i in range(0, len(self.data.index), 60)]
    axis_6 = [(i, list(self.data.index)[i]) for i in range(0, len(self.data.index), 120)]
    stringaxis = pg.AxisItem(orientation='bottom')  # 创建一个刻度项
    stringaxis.setTicks([axis_6,axis_5, axis_4, axis_3, axis_2, axis_1, self.axis_dict.items()])  # 设置X轴刻度值
    self.k_plt.getAxis("bottom").setTicks([axis_6,axis_5, axis_4, axis_3, axis_2, axis_1, self.axis_dict.items()])
    self.k_plt.plotItem.clear()  # 清空绘图部件中的项
    item = CandlestickItem(data_list)  # 生成蜡烛图数据
    self.k_plt.addItem(item, )  # 在绘图部件中添加蜡烛图项目
    self.k_plt.showGrid(x=True, y=True)  # 设置绘图部件显示网格线
    self.k_plt.setYRange(y_min, y_max)
    self.k_plt.setLabel(axis='left', text='指数')  # 设置Y轴标签
    self.k_plt.setLabel(axis='bottom', text='日期')  # 设置X轴标签
    self.label = pg.TextItem()  # 创建一个文本项
    self.k_plt.addItem(self.label)  #
    self.move_slot = pg.SignalProxy(self.k_plt.scene().sigMouseMoved, rateLimit=60, slot=self.print_slot)

    self.vLine = pg.InfiniteLine(angle=90, movable=False, )  # 创建一个垂直线条
    self.hLine = pg.InfiniteLine(angle=0, movable=False, )  # 创建一个水平线条
    self.k_plt.addItem(self.vLine, ignoreBounds=True)  # 在图形部件中添加垂直线条
    self.k_plt.addItem(self.hLine, ignoreBounds=True)  # 在图形部件中添加水平线条


class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data  # data里面必须有以下字段: 时间, 开盘价, 收盘价, 最低价, 最高价
        self.generatePicture()

    def generatePicture(self):
        self.picture = PyQt5.QtGui.QPicture()  # 实例化一个绘图设备
        p = PyQt5.QtGui.QPainter(self.picture)  # 在picture上实例化QPainter用于绘图
        p.setPen(pg.mkPen('w'))  # 设置画笔颜色
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for t, open, close, min, max in self.data:
            if open > close:  # 开盘价大于收盘价
                p.setPen(pg.mkPen('g'))
                p.setBrush(pg.mkBrush('g'))  # 设置画刷颜色为绿
            else:
                p.setPen(pg.mkPen('r'))
                p.setBrush(pg.mkBrush('r'))  # 设置画刷颜色为红\
            p.drawLine(PyQt5.QtCore.QPointF(t, min), PyQt5.QtCore.QPointF(t, max))  # 绘制线条
            p.drawRect(PyQt5.QtCore.QRectF(t - w, open, w * 2, close - open))  # 绘制箱子
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return PyQt5.QtCore.QRectF(self.picture.boundingRect())


