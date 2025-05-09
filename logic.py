from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_submit.clicked.connect(lambda: self.submit())




    def submit(self):
        try:
         id_num = int(self.input_id.text())
         self.cast_vote()
         print(id_num)
         self.input_id.setText('')

        except ValueError:
            self.label_result.setText(f'ID must only use digits [0-9]')
            self.input_id.setText('')
        except Warning:
            self.label_result.setText(f'Please select candidate')
            self.input_id.setText('')

    def cast_vote(self):
        if self.radio_bianca.isChecked():
            print('bianca')
        elif self.radio_edward.isChecked():
            print('edward')
        elif self.radio_felicia.isChecked():
            print('felicia')
        else:
            raise Warning


