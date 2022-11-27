import sys
from PyQt5.QtWidgets import *
# from PyQt5 import uic
from graphbuild_demo_3 import Ui_MainWindow
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
# from matplotlib import font_manager, rc
from superqt import QRangeSlider

# font_path = "C:/Users/XOTOURLLIFE/AppData/Local/Microsoft/Windows/Fonts/gulim.ttc"
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)

# hello
class graphBuilder(QMainWindow):
    def __init__(self):
        super(graphBuilder, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('GraphBuilder')
        # self.center()

        self.map = MapCanvas(self, self.ui.graph_frame.width()/100, self.ui.graph_frame.height()/100)
        self.ui.graph_frame.layout().addWidget(self.map)
        self.toolbar = NavigationToolbar(self.map, self)
        self.ui.graph_frame.layout().addWidget(self.toolbar)

        self.ui.lineEdit_x_label.textChanged[str].connect(self.map.onXLabelChanged)
        self.ui.lineEdit_y_label.textChanged[str].connect(self.map.onYLabelChanged)
        self.ui.comboBox_line.activated[str].connect(self.map.LineChanged)
        self.ui.pushButton_2.clicked.connect(self.graphBuildButton)
        self.ui.pushButton_clear.clicked.connect(self.map.clear_map)

        # self.ui.textEdit_data
    

    def graphBuildButton(self):
        x_input = self.ui.lineEdit_x_value.text()
        x_input = x_input.replace(" " , "")
        x_input_list = x_input.split(',')

        y_input = self.ui.lineEdit_y_value.text()
        y_input = y_input.replace(" " , "")
        y_input_list = y_input.split(',')

        if x_input_list==[''] or y_input_list==['']:
            reply = QMessageBox.question(self, 'Alarm', 'You didnt input any values', QMessageBox.No, QMessageBox.No)
            self.ui.lineEdit_x_value.setText('')
            self.ui.lineEdit_y_value.setText('')
        else:
            for i in range(len(x_input_list)):
                x_input_list[i] = int(x_input_list[i])
            self.map.x_data = x_input_list

            for i in range(len(y_input_list)):
                y_input_list[i] = int(y_input_list[i])
            self.map.y_data = y_input_list

            self.map.plot_map()

        # print(self.map.y_data)

    # def initUI(self):
    #     self.setWindowTitle('GraphBuilder')
    #     # self.resize(500, 350)
    #     # self.center()
    #     self.show()

    # def graphBuildButton(self):

    #     canvas = FigureCanvas(Figure(figsize=(4, 3)))
    #     self.verticalLayout.addWidget(canvas)

    #     self.addToolBar(NavigationToolbar(canvas, self))

    #     # self.ax = canvas.figure.subplots()
    #     # self.ax.plot([0, 1, 2], [1, 5, 3], '-')




    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class MapCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        self.axes = self.fig.add_subplot(111)
        self.x_data = [0, 1, 2]
        self.y_data = [1, 5, 3]
        self.cs = None

        self.plot_map()

    def Return_Min(self, data_list):
        min = 10000
        for i in range(len(data_list)):
            if data_list[i] < min:
                min = data_list[i]

        return min

    def Return_Max(self, data_list):
        max = 0
        for i in range(len(data_list)):
            if data_list[i] > max:
                max = data_list[i]

        return max
            

    def plot_map(self, date=None):
        self.axes.plot(self.x_data, self.y_data, '-')
        self.axes.set_xlim([self.Return_Min(self.x_data), self.Return_Max(self.x_data)])
        self.axes.set_ylim([self.Return_Min(self.y_data), self.Return_Max(self.y_data)])
        self.draw()
    
    def clear_map(self):
        self.axes.clear()
        self.draw()

    def set_x_lim(self, leftValue=0, RightValue=5):
        self.axes.set_xlim(left= leftValue, right=RightValue)

    def set_y_lim(self, leftValue=0, RightValue=5):
        self.axes.set_ylim(left= leftValue, right=RightValue)

    def graphBuildButton(self):
        self.plt.set_ydata


    def onXLabelChanged(self, text):
        self.axes.set_xlabel(text)
        self.draw()
        
    def onYLabelChanged(self, text):
        self.axes.set_ylabel(text)
        self.draw()

    def LineChanged(self, text):
        if text == "solid line style":
            # solid line style
            self.axes.plot(self.x_data, self.y_data, '-')
            self.draw()
        elif text == "dashed line style":
            # dashed line style
            self.axes.plot(self.x_data, self.y_data, '--')
            self.draw()
        elif text == "dash-dot line style":
            # dash-dot line style
            self.axes.plot(self.x_data, self.y_data, '-.')
            self.draw()
        else:
            self.axes.plot(self.x_data, self.y_data, ':')
            self.draw()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = graphBuilder()
    myWindow.show()
    sys.exit(app.exec_())