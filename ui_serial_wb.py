# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serial_wb.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(690, 608)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(600, 514))
        MainWindow.setMaximumSize(QSize(970, 742))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.Label_COM = QLabel(self.groupBox)
        self.Label_COM.setObjectName(u"Label_COM")
        self.Label_COM.setMinimumSize(QSize(0, 25))
        self.Label_COM.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        self.Label_COM.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Label_COM)

        self.Combo_COM = QComboBox(self.groupBox)
        self.Combo_COM.setObjectName(u"Combo_COM")
        sizePolicy1.setHeightForWidth(self.Combo_COM.sizePolicy().hasHeightForWidth())
        self.Combo_COM.setSizePolicy(sizePolicy1)
        self.Combo_COM.setMinimumSize(QSize(0, 25))
        self.Combo_COM.setMaximumSize(QSize(16777215, 40))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Combo_COM)

        self.Label_Baurdate = QLabel(self.groupBox)
        self.Label_Baurdate.setObjectName(u"Label_Baurdate")
        self.Label_Baurdate.setMinimumSize(QSize(0, 25))
        self.Label_Baurdate.setMaximumSize(QSize(16777215, 40))
        self.Label_Baurdate.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.Label_Baurdate)

        self.Combo_Baudrate = QComboBox(self.groupBox)
        self.Combo_Baudrate.addItem("")
        self.Combo_Baudrate.addItem("")
        self.Combo_Baudrate.addItem("")
        self.Combo_Baudrate.addItem("")
        self.Combo_Baudrate.addItem("")
        self.Combo_Baudrate.addItem("")
        self.Combo_Baudrate.addItem("")
        self.Combo_Baudrate.addItem("")
        self.Combo_Baudrate.addItem("")
        self.Combo_Baudrate.addItem("")
        self.Combo_Baudrate.setObjectName(u"Combo_Baudrate")
        self.Combo_Baudrate.setMinimumSize(QSize(0, 25))
        self.Combo_Baudrate.setMaximumSize(QSize(16777215, 40))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Combo_Baudrate)

        self.Label_Data_bit = QLabel(self.groupBox)
        self.Label_Data_bit.setObjectName(u"Label_Data_bit")
        self.Label_Data_bit.setMinimumSize(QSize(0, 25))
        self.Label_Data_bit.setMaximumSize(QSize(16777215, 40))
        self.Label_Data_bit.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.Label_Data_bit)

        self.Combo_Data_bit = QComboBox(self.groupBox)
        self.Combo_Data_bit.addItem("")
        self.Combo_Data_bit.addItem("")
        self.Combo_Data_bit.addItem("")
        self.Combo_Data_bit.addItem("")
        self.Combo_Data_bit.setObjectName(u"Combo_Data_bit")
        self.Combo_Data_bit.setMinimumSize(QSize(0, 25))
        self.Combo_Data_bit.setMaximumSize(QSize(16777215, 40))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Combo_Data_bit)

        self.Label_Parity = QLabel(self.groupBox)
        self.Label_Parity.setObjectName(u"Label_Parity")
        self.Label_Parity.setMinimumSize(QSize(0, 25))
        self.Label_Parity.setMaximumSize(QSize(16777215, 40))
        self.Label_Parity.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.Label_Parity)

        self.Combo_Parity = QComboBox(self.groupBox)
        self.Combo_Parity.addItem("")
        self.Combo_Parity.addItem("")
        self.Combo_Parity.addItem("")
        self.Combo_Parity.setObjectName(u"Combo_Parity")
        self.Combo_Parity.setMinimumSize(QSize(0, 25))
        self.Combo_Parity.setMaximumSize(QSize(16777215, 40))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.Combo_Parity)

        self.Label_Stop_bit = QLabel(self.groupBox)
        self.Label_Stop_bit.setObjectName(u"Label_Stop_bit")
        self.Label_Stop_bit.setMinimumSize(QSize(0, 25))
        self.Label_Stop_bit.setMaximumSize(QSize(16777215, 40))
        self.Label_Stop_bit.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.Label_Stop_bit)

        self.Combo_Stop_bit = QComboBox(self.groupBox)
        self.Combo_Stop_bit.addItem("")
        self.Combo_Stop_bit.addItem("")
        self.Combo_Stop_bit.addItem("")
        self.Combo_Stop_bit.setObjectName(u"Combo_Stop_bit")
        self.Combo_Stop_bit.setMinimumSize(QSize(0, 25))
        self.Combo_Stop_bit.setMaximumSize(QSize(16777215, 40))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.Combo_Stop_bit)


        self.verticalLayout.addLayout(self.formLayout)

        self.Button_Onoff_com = QPushButton(self.groupBox)
        self.Button_Onoff_com.setObjectName(u"Button_Onoff_com")
        self.Button_Onoff_com.setFont(font)

        self.verticalLayout.addWidget(self.Button_Onoff_com)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Button_Clear_display = QPushButton(self.groupBox)
        self.Button_Clear_display.setObjectName(u"Button_Clear_display")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(False)
        self.Button_Clear_display.setFont(font1)

        self.verticalLayout.addWidget(self.Button_Clear_display)

        self.Box_Display_hex = QCheckBox(self.groupBox)
        self.Box_Display_hex.setObjectName(u"Box_Display_hex")

        self.verticalLayout.addWidget(self.Box_Display_hex)

        self.Box_Auto_wrap = QCheckBox(self.groupBox)
        self.Box_Auto_wrap.setObjectName(u"Box_Auto_wrap")

        self.verticalLayout.addWidget(self.Box_Auto_wrap)

        self.Box_Display_send = QCheckBox(self.groupBox)
        self.Box_Display_send.setObjectName(u"Box_Display_send")

        self.verticalLayout.addWidget(self.Box_Display_send)

        self.Box_Display_time = QCheckBox(self.groupBox)
        self.Box_Display_time.setObjectName(u"Box_Display_time")

        self.verticalLayout.addWidget(self.Box_Display_time)

        self.verticalSpacer_2 = QSpacerItem(78, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.groupBox)

        self.Textbrowser_Receive = QTextBrowser(self.groupBox_2)
        self.Textbrowser_Receive.setObjectName(u"Textbrowser_Receive")

        self.horizontalLayout.addWidget(self.Textbrowser_Receive)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Box_Periodic_send = QCheckBox(self.groupBox_3)
        self.Box_Periodic_send.setObjectName(u"Box_Periodic_send")
        self.Box_Periodic_send.setMinimumSize(QSize(50, 0))
        self.Box_Periodic_send.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.Box_Periodic_send)

        self.LineEdit_Ms = QLineEdit(self.groupBox_3)
        self.LineEdit_Ms.setObjectName(u"LineEdit_Ms")
        self.LineEdit_Ms.setMinimumSize(QSize(50, 20))
        self.LineEdit_Ms.setMaximumSize(QSize(60, 25))

        self.horizontalLayout_2.addWidget(self.LineEdit_Ms)

        self.Label_Ms = QLabel(self.groupBox_3)
        self.Label_Ms.setObjectName(u"Label_Ms")
        self.Label_Ms.setMinimumSize(QSize(50, 0))
        self.Label_Ms.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.Label_Ms)

        self.Box_Hex_send = QCheckBox(self.groupBox_3)
        self.Box_Hex_send.setObjectName(u"Box_Hex_send")
        self.Box_Hex_send.setMinimumSize(QSize(50, 0))
        self.Box_Hex_send.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.Box_Hex_send)

        self.Button_Clear_send = QPushButton(self.groupBox_3)
        self.Button_Clear_send.setObjectName(u"Button_Clear_send")
        self.Button_Clear_send.setMinimumSize(QSize(60, 25))
        self.Button_Clear_send.setMaximumSize(QSize(80, 35))

        self.horizontalLayout_2.addWidget(self.Button_Clear_send)

        self.Button_Send = QPushButton(self.groupBox_3)
        self.Button_Send.setObjectName(u"Button_Send")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Button_Send.sizePolicy().hasHeightForWidth())
        self.Button_Send.setSizePolicy(sizePolicy2)
        self.Button_Send.setMinimumSize(QSize(60, 25))
        self.Button_Send.setMaximumSize(QSize(80, 35))

        self.horizontalLayout_2.addWidget(self.Button_Send)

        self.TextEdit_Send = QTextEdit(self.groupBox_3)
        self.TextEdit_Send.setObjectName(u"TextEdit_Send")
        sizePolicy1.setHeightForWidth(self.TextEdit_Send.sizePolicy().hasHeightForWidth())
        self.TextEdit_Send.setSizePolicy(sizePolicy1)
        self.TextEdit_Send.setMinimumSize(QSize(0, 40))
        self.TextEdit_Send.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_2.addWidget(self.TextEdit_Send)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 690, 23))
        self.menubar.setDefaultUp(False)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u63a5\u53d7\u533a", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u914d\u7f6e\u533a", None))
        self.Label_COM.setText(QCoreApplication.translate("MainWindow", u"COM\u53e3", None))
        self.Label_Baurdate.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387", None))
        self.Combo_Baudrate.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.Combo_Baudrate.setItemText(1, QCoreApplication.translate("MainWindow", u"19200", None))
        self.Combo_Baudrate.setItemText(2, QCoreApplication.translate("MainWindow", u"38400", None))
        self.Combo_Baudrate.setItemText(3, QCoreApplication.translate("MainWindow", u"57600", None))
        self.Combo_Baudrate.setItemText(4, QCoreApplication.translate("MainWindow", u"115200", None))
        self.Combo_Baudrate.setItemText(5, QCoreApplication.translate("MainWindow", u"230400", None))
        self.Combo_Baudrate.setItemText(6, QCoreApplication.translate("MainWindow", u"460800", None))
        self.Combo_Baudrate.setItemText(7, QCoreApplication.translate("MainWindow", u"921600", None))
        self.Combo_Baudrate.setItemText(8, QCoreApplication.translate("MainWindow", u"1000000", None))
        self.Combo_Baudrate.setItemText(9, QCoreApplication.translate("MainWindow", u"2000000", None))

        self.Label_Data_bit.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4f4d", None))
        self.Combo_Data_bit.setItemText(0, QCoreApplication.translate("MainWindow", u"8", None))
        self.Combo_Data_bit.setItemText(1, QCoreApplication.translate("MainWindow", u"7", None))
        self.Combo_Data_bit.setItemText(2, QCoreApplication.translate("MainWindow", u"6", None))
        self.Combo_Data_bit.setItemText(3, QCoreApplication.translate("MainWindow", u"5", None))

        self.Label_Parity.setText(QCoreApplication.translate("MainWindow", u"\u6821\u9a8c\u4f4d", None))
        self.Combo_Parity.setItemText(0, QCoreApplication.translate("MainWindow", u"N", None))
        self.Combo_Parity.setItemText(1, QCoreApplication.translate("MainWindow", u"O", None))
        self.Combo_Parity.setItemText(2, QCoreApplication.translate("MainWindow", u"E", None))

        self.Label_Stop_bit.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u4f4d", None))
        self.Combo_Stop_bit.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.Combo_Stop_bit.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.Combo_Stop_bit.setItemText(2, QCoreApplication.translate("MainWindow", u"1.5", None))

        self.Button_Onoff_com.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4e32\u53e3", None))
        self.Button_Clear_display.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u63a5\u6536\u533a", None))
        self.Box_Display_hex.setText(QCoreApplication.translate("MainWindow", u"hex\u663e\u793a", None))
        self.Box_Auto_wrap.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u6362\u884c", None))
        self.Box_Display_send.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u53d1\u9001", None))
        self.Box_Display_time.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u65f6\u95f4", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u53d1\u5c04\u533a", None))
        self.Box_Periodic_send.setText(QCoreApplication.translate("MainWindow", u"\u5b9a\u65f6", None))
        self.LineEdit_Ms.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.Label_Ms.setText(QCoreApplication.translate("MainWindow", u"ms/\u6b21", None))
        self.Box_Hex_send.setText(QCoreApplication.translate("MainWindow", u"hex", None))
        self.Button_Clear_send.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.Button_Send.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"&", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"&\u6e29\u535a\u4e32\u53e3\u52a9\u624bV0.1", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"&For MGWQ", None))
    # retranslateUi

