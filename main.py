import threading
import sys
import time
import serial
from datetime import datetime
import serial.tools.list_ports                                     # 很重要的一个类
from ui_serial_wb import Ui_MainWindow

from PySide6.QtGui import QColor, QIcon,QAction
from PySide6.QtCore import (QTimer, Signal)
from PySide6.QtWidgets import (QMainWindow, QApplication,QMessageBox,QWidgetAction)
import base64, os
from qt_material import apply_stylesheet,list_themes


class SerialTool(QMainWindow, Ui_MainWindow):
    signalRecieve = Signal(object)

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setupUi_my()
        self.refreshPort()
        self.InitUIEvent()         #   初始化ui事件
        self.initCOM()             #   串口初始化
        self.init_timer()          #   初始化定时器
        #   收到串口数据后会启动槽函数， 执行uart_receive_display函数
        self.signalRecieve.connect(self.uart_receive_display)

    def setupUi_my(self):

        theme = self.menubar.addMenu('主题切换')
        qt_m = QAction('Qt_Material',self)
        theme.addAction(qt_m)

        for item in list_themes():
            th = QAction(item,self)
            theme.addAction(th)
            th.triggered.connect(self.change_theme)


    def change_theme(self):
        action = self.sender()
        theme_name = action.text()
        apply_stylesheet(app, theme=theme_name)

    def init_timer(self):
        self.timer_send = QTimer(self)
        self.timer_send.timeout.connect(self.UartSend)


    ''' 
    # 如果线程挂载这个函数，当线程thread启动后，就回每隔一段时间去自动调用这个程序
    # 而不会让这个程序阻塞住，像单片机的while(1) ，如果没有操作系统，就是死循环，什么也干不了
    def temp(self):
        while True:
            print('123')
            time.sleep(0.1)
    '''
    #刷新串口，读取串口设备
    def refreshPort(self):
        self.com_list = []
        port_list = list(serial.tools.list_ports.comports())    #读取串口 返回列表 ,在这里并没有创建串口对象
        self.Combo_COM.clear()
        if len(port_list) > 0:
            for port_com in port_list:                  # 遍历串口
                #port_serial = list(port_com)[0]         # 就是port_com.device
                port_serial = port_com.device
                self.Combo_COM.addItem(port_serial)
                self.com_list.append(port_serial)
        else:
            self.Combo_COM.addItem('')

    # 初始化串口，我认为这里是装载UI界面上默认的参数
    def initCOM(self):
        self.l_serial = serial.Serial()             # l_serial就是一个串口对象
        if (len(self.com_list)):
            self.l_serial.port = self.Combo_COM.currentText()
        self.l_serial.baudrate = int(self.Combo_Baudrate.currentText())
        self.l_serial.bytesize = int(self.Combo_Data_bit.currentText())
        self.l_serial.stopbits = int(self.Combo_Stop_bit.currentText())
        self.l_serial.parity = self.Combo_Parity.currentText()
        # serial.PARITY_NONE
        self.l_serial.timeout = 0.2

    def InitUIEvent(self):
            self.Combo_COM.activated.connect(self.ComActivated)                # 串口port属性
            self.Combo_COM.popupAboutToBeShown.connect(self.RefreshComActivated)
            self.Combo_Baudrate.activated.connect(self.BaudActivated)
            self.Combo_Parity.activated.connect(self.ParityBitActivated)
            self.Combo_Data_bit.activated.connect(self.DataBitActivated)
            self.Combo_Stop_bit.activated.connect(self.StopBitActivated)

            self.Button_Onoff_com.clicked.connect(self.OpenSerial)     #按键打开串口也会启动创建线程
            self.Button_Clear_display.clicked.connect(self.ClearReceiveActivated)

            #这里的 lambda函数 必不可少
            self.Box_Display_hex.stateChanged.connect(lambda: self.CheckActivated(self.Box_Display_hex))
            self.Box_Auto_wrap.stateChanged.connect(lambda: self.CheckActivated(self.Box_Auto_wrap))
            self.Box_Display_send.stateChanged.connect(lambda: self.CheckActivated(self.Box_Display_send))
            self.Box_Display_time.stateChanged.connect(lambda: self.CheckActivated(self.Box_Display_time))
            #发射-定时 起作用
            self.Box_Periodic_send.stateChanged.connect(lambda: self.CheckActivated(self.Box_Periodic_send))
            self.Box_Hex_send.stateChanged.connect(lambda: self.CheckActivated(self.Box_Hex_send))

            # self.Button_Clear_send.clicked.connect(self.ClearSendActivated)
            self.Button_Send.clicked.connect(self.UartSend)

    # 串口对象的port属性

    def RefreshComActivated(self):
        self.refreshPort()
        if (len(self.com_list)):
            self.l_serial.port = self.com_list[0]
            # print(l_serial.port)
        print(self.com_list[0])


    def ComActivated(self, text):
        self.l_serial.port = self.Combo_COM.itemText(text)
        print(f'当前选中的COM是：{ self.l_serial.port}')
        print(f'当前选波特率：{self.l_serial.baudrate}')
        print(f'当前校验位：{self.l_serial.parity}')
        print(f'当前数据位：{self.l_serial.bytesize}')
        print(f'当前停止位：{self.l_serial.stopbits}')

    def BaudActivated(self, text):
        self.l_serial.baudrate = int(self.Combo_Baudrate.itemText(text))
        print(self.l_serial.baudrate )

    def ParityBitActivated(self, index):

        text = self.Combo_Parity.itemText(index)
        print(text)
        if (text == 'N'):
            self.l_serial.parity = serial.PARITY_NONE
        elif (text == 'O'):
            self.l_serial.parity = serial.PARITY_ODD
        elif (text == 'E'):
            self.l_serial.parity = serial.PARITY_EVEN

    def DataBitActivated(self, text):
        # 这里要传入 int ，而不是str
        self.l_serial.bytesize = int(self.Combo_Data_bit.itemText(text))
        print(self.l_serial.bytesize)

    def StopBitActivated(self, text):   #停止位设置
        self.l_serial.stopbits = int(self.Combo_Stop_bit.itemText(text))

    # QCheckBox的公共相应函数
    def CheckActivated(self, BtnCheck):

        # 这段if 判断是判断 定时发送的 QCheckBox的功能
        if BtnCheck == self.Box_Periodic_send:          # 发射区的  定时check_box
            if self.Box_Periodic_send.isChecked():      # 在pyside6中用ischecked 检查QCheckBox的状态
                if self.l_serial.isOpen():
                    time = self.LineEdit_Ms.text()
                    time_val = int(time, 10)
                    if time_val > 0:
                        self.timer_send.start(time_val)     # 开启定时器，参数为设置 时长
            else:
                self.timer_send.stop()                  #定时器关闭


    def ClearReceiveActivated(self):
        self.Textbrowser_Receive.setPlainText('')


    #启动，停用串口功能
    def OpenSerial(self):

        if self.l_serial.isOpen():              #下面的代码是关闭串口
            # self.timer_send.stop()
            #self.thread_read.join()
            self.l_serial.close()
            self.Button_Onoff_com.setText("打开串口")
            self.Textbrowser_Receive.setPlainText('')
            self.Combo_COM.setEnabled(True)
            self.Combo_Baudrate.setEnabled(True)
            self.Combo_Data_bit.setEnabled(True)
            self.Combo_Stop_bit.setEnabled(True)
            self.Combo_Parity.setEnabled(True)
            self.timer_send.stop()              # 定时器关闭
                                                # 取消定时器状态

        else:                                   # 下面的代码是打开串口
            self.l_serial.open()
            self.Button_Onoff_com.setText("关闭串口")

            self.Combo_COM.setEnabled(False)
            self.Combo_Baudrate.setEnabled(False)
            self.Combo_Data_bit.setEnabled(False)
            self.Combo_Stop_bit.setEnabled(False)
            self.Combo_Parity.setEnabled(False)

            # 打开串口需要开启线程 ，线程的作用是检测串口的接收数据
            self.thread_read = None
            self.thread_read = threading.Thread(target=self.UartRead)  # 创建线程对象，
            # self.thread_read = threading.Thread(target=self.temp)       # 线程测试用例
            self.thread_read.Daemon = True
            self.thread_read.start()             #进程开启 ,线程只允许启动一次

    def uart_receive_display(self, obj):
        now_time = datetime.now()                                   # 获取当前时间
        new_time = now_time.strftime('[%H:%M:%S:%f]')

        # --------------- 关于是否hex显示的问题 --------------------------------------
        if self.Box_Display_hex.isChecked():                       # hex显示
            # ---------------------- 关于是否显示时间 ---------------------
            if self.Box_Display_time.isChecked():                   # 显示时间
                self.recv_data = '\r\n' + new_time + obj.strip()
            else:
                self.recv_data = obj.strip()                        #2进制显示已经转字符串了

        else:  # 普通显示模式 来的数据依然是bytes 需要先解码
            # ---------------------- 关于是否显示时间 ---------------------
            if self.Box_Display_time.isChecked(): # 需要显示时间
                self.recv_data = '\r\n' + new_time + obj.decode('utf-8', "ignore")
            else:
                self.recv_data = obj.decode('utf-8', "ignore")

        if self.Box_Display_send.isChecked():  # 输入显示发送的话，接收到的数据就要加上[Receive]:
            self.recv_data = '\r\n' + '[Receive]:' + self.recv_data

        if self.Box_Auto_wrap.checkState():  # 显示模式
            self.Textbrowser_Receive.append(self.recv_data)

        else:
            self.Textbrowser_Receive.insertPlainText(self.recv_data)
        # 文本框显示到底部
        self.Textbrowser_Receive.moveCursor(self.Textbrowser_Receive.textCursor().End)

    # time.sleep(0.2)

    '''
    串口读函数
    这个是被thread.read进程调用的函数,串口打开就会循环读取串口的接收指
    serial.inWaiting() 方法就是不断的读取 接收缓冲区的数值
    字符串格式化功能  '{:02X}' ,等价为 '{0:02X}'以为format()默认是一个参数，
    02 表示输出的十六进制数至少要有两位，如果不足两位则在前面补0。
    X 表示以十六进制（大写字母）形式输出
    因此，如果self.data[i]是10（十进制），那么格式化后的字符串将是'0A'。
    '''
    def UartRead(self):

        print('我是被进程调用的函数UartRead')
        while self.l_serial.isOpen():

            num = self.l_serial.inWaiting()
            if num:
                self.data = self.l_serial.read(num)   # self.data 就是 bytes类
                if self.Box_Display_hex.isChecked():  # hex 显示
                    hex_data = ''
                    for i in range(0, len(self.data)): #从bytes中取一个字节
                        hex_data = hex_data + '{:02X}'.format(self.data[i]) + ' ' #进行字符串格式化
                    # self.Textbrowser_Receive.append(hex_data.strip())
                    self.signalRecieve.emit(hex_data)                           # 将数据发送出去
                else:
                    # self.Textbrowser_Receive.append(data.decode().strip())
                    # self.Textbrowser_Receive.insertPlainText(data.decode('utf-8',"ignore"))
                    self.signalRecieve.emit(self.data)      # 数据传到槽函数中进行deencode解码

            time.sleep(0.1)

    def UartSend(self):

        if self.l_serial.isOpen():
            InputStr = self.TextEdit_Send.toPlainText()

            if InputStr == '' :
                return
            if self.Box_Display_send.isChecked():
                self.recv_data = '[Send] ' + InputStr
                self.Textbrowser_Receive.append(self.recv_data)

            if self.Box_Hex_send.isChecked():

                InputStr =InputStr.strip()
                send_lst=[]

                while InputStr != '':

                    try:

                        num = int(InputStr[0:2],16)               #这里出问题会抛出异常
                        send_lst.append(num)
                        InputStr = InputStr[2:]         #右移两位数据
                        InputStr = InputStr.strip()

                    except ValueError:

                        QMessageBox.critical(self,'pycom','请输入十六进制数据，以空格结束！')
                        return None

                InputStr = bytes(send_lst)
                self.l_serial.write(InputStr)
            else:
                self.l_serial.write(InputStr.encode()+b'\0')

        else:
            QMessageBox.critical(self,'error','串口未连接！')



if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = SerialTool()

    ex.show()

    sys.exit(app.exec())