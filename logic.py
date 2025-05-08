from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.button_submit.clicked.connect(lambda: self.submit())


	def submit(self):
		try:
			id_num = self.input_id.text()
			print(id_num)

		except ValueError:
			self.label_result.setText(f'ID must only use digits [0-9]')




