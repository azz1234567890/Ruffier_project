from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
from instr import*

class FinalWin(QWidget):
   def __init__(self):
          super().__init__()
          self.initUI()
          self.set_appear()
          self.show()

   def initUI(self):
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.workh_text, alignment= Qt.AlignCenter)
        self.layout_line.addWidget(self.index_text, alignment= Qt.AlignCenter)
        self.setLayout(self.layout_line)

   def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


