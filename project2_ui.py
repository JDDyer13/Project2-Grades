# Form implementation generated from reading ui file 'project2_ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(413, 137)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 179, 179))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 179, 179))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 179, 179))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 179, 179))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(30, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_name.setFont(font)
        self.label_name.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_name.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_name.setObjectName("label_name")
        self.input_name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_name.setGeometry(QtCore.QRect(180, 30, 181, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.input_name.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.input_name.setFont(font)
        self.input_name.setObjectName("input_name")
        self.label_attempts = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_attempts.setGeometry(QtCore.QRect(30, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_attempts.setFont(font)
        self.label_attempts.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_attempts.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_attempts.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_attempts.setObjectName("label_attempts")
        self.input_attempts = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_attempts.setGeometry(QtCore.QRect(180, 70, 181, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.input_attempts.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.input_attempts.setFont(font)
        self.input_attempts.setObjectName("input_attempts")
        self.label_score_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_score_1.setGeometry(QtCore.QRect(80, 140, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_score_1.setFont(font)
        self.label_score_1.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_score_1.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_score_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_score_1.setObjectName("label_score_1")
        self.label_score_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_score_2.setGeometry(QtCore.QRect(80, 190, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_score_2.setFont(font)
        self.label_score_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_score_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_score_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_score_2.setObjectName("label_score_2")
        self.label_score_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_score_3.setGeometry(QtCore.QRect(80, 240, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_score_3.setFont(font)
        self.label_score_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_score_3.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_score_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_score_3.setObjectName("label_score_3")
        self.label_score_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_score_4.setGeometry(QtCore.QRect(80, 290, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_score_4.setFont(font)
        self.label_score_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_score_4.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_score_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_score_4.setObjectName("label_score_4")
        self.input_score_1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_score_1.setGeometry(QtCore.QRect(190, 150, 91, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.input_score_1.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.input_score_1.setFont(font)
        self.input_score_1.setObjectName("input_score_1")
        self.input_score_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_score_2.setGeometry(QtCore.QRect(190, 200, 91, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.input_score_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.input_score_2.setFont(font)
        self.input_score_2.setObjectName("input_score_2")
        self.input_score_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_score_3.setGeometry(QtCore.QRect(190, 250, 91, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.input_score_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.input_score_3.setFont(font)
        self.input_score_3.setObjectName("input_score_3")
        self.input_score_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_score_4.setGeometry(QtCore.QRect(190, 300, 91, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.input_score_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.input_score_4.setFont(font)
        self.input_score_4.setObjectName("input_score_4")
        self.button_submit4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_submit4.setGeometry(QtCore.QRect(100, 340, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_submit4.setFont(font)
        self.button_submit4.setObjectName("button_submit4")
        self.label_submit4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_submit4.setGeometry(QtCore.QRect(110, 380, 151, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_submit4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_submit4.setFont(font)
        self.label_submit4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_submit4.setObjectName("label_submit4")
        self.button_enter = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(100, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_enter.setFont(font)
        self.button_enter.setObjectName("button_enter")
        self.button_submit1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_submit1.setGeometry(QtCore.QRect(100, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_submit1.setFont(font)
        self.button_submit1.setObjectName("button_submit1")
        self.button_submit2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_submit2.setGeometry(QtCore.QRect(100, 240, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_submit2.setFont(font)
        self.button_submit2.setObjectName("button_submit2")
        self.button_submit3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_submit3.setGeometry(QtCore.QRect(100, 290, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_submit3.setFont(font)
        self.button_submit3.setObjectName("button_submit3")
        self.label_submit1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_submit1.setGeometry(QtCore.QRect(110, 230, 151, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_submit1.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_submit1.setFont(font)
        self.label_submit1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_submit1.setObjectName("label_submit1")
        self.label_submit2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_submit2.setGeometry(QtCore.QRect(110, 280, 151, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_submit2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_submit2.setFont(font)
        self.label_submit2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_submit2.setObjectName("label_submit2")
        self.label_submit3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_submit3.setGeometry(QtCore.QRect(110, 330, 151, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_submit3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_submit3.setFont(font)
        self.label_submit3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_submit3.setObjectName("label_submit3")
        self.label_score_1.hide()
        self.label_score_2.hide()
        self.label_score_3.hide()
        self.label_score_4.hide()
        self.input_score_1.hide()
        self.input_score_2.hide()
        self.input_score_3.hide()
        self.input_score_4.hide()
        self.button_submit1.hide()
        self.label_submit1.hide()
        self.button_submit2.hide()
        self.label_submit2.hide()
        self.button_submit3.hide()
        self.label_submit3.hide()
        self.button_submit4.hide()
        self.label_submit4.hide()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grade Submission"))
        self.label_name.setText(_translate("MainWindow", "Enter Student Name: "))
        self.input_name.setText(_translate("MainWindow", ""))
        self.label_attempts.setText(_translate("MainWindow", "# of Attempts: "))
        self.input_attempts.setText(_translate("MainWindow", ""))
        self.label_score_1.setText(_translate("MainWindow", "Score 1:"))
        self.label_score_2.setText(_translate("MainWindow", "Score 2:"))
        self.label_score_3.setText(_translate("MainWindow", "Score 3:"))
        self.label_score_4.setText(_translate("MainWindow", "Score 4:"))
        self.input_score_1.setText(_translate("MainWindow", ""))
        self.input_score_2.setText(_translate("MainWindow", ""))
        self.input_score_3.setText(_translate("MainWindow", ""))
        self.input_score_4.setText(_translate("MainWindow", ""))
        self.button_submit4.setText(_translate("MainWindow", "Submit"))
        self.label_submit4.setText(_translate("MainWindow", "Submitted!"))
        self.button_enter.setText(_translate("MainWindow", "Enter"))
        self.button_submit1.setText(_translate("MainWindow", "Submit"))
        self.button_submit2.setText(_translate("MainWindow", "Submit"))
        self.button_submit3.setText(_translate("MainWindow", "Submit"))
        self.label_submit1.setText(_translate("MainWindow", "Submitted!"))
        self.label_submit2.setText(_translate("MainWindow", "Submitted!"))
        self.label_submit3.setText(_translate("MainWindow", "Submitted!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
