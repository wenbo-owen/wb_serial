from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Signal

class MyQComBox(QComboBox):
    popupAboutToBeShown = Signal()  # 创建一个信号

    def showPopup(self):                        # 重写showPopup函数
        super(MyQComBox, self).showPopup()      # 调用父类shoWPopup()方法
        self.popupAboutToBeShown.emit()         # 发送信号