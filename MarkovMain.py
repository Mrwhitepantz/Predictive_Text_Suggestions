from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MarkovWindow import *

app = QApplication([])
window = MarkovWindow()
window.show()
app.exec_()
