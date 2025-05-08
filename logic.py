from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.button_submit.clicked.connect(lambda: self.submit())

	def submit(self):
		pass


