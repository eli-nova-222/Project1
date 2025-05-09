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
         print(self.cast_vote())

         #reset if correct
         self.label_result.setText('VOTE SUBMITTED')
         self.input_id.setText('')

        #exception for non-int id num
        except ValueError:
            self.label_result.setText(f'ID must only use digits [0-9]')
            self.input_id.setText('')

        #exception for no candidate selected
        except Warning:
            self.label_result.setText(f'Please select candidate')
            self.input_id.setText('')

    # retrieves button vote
    def cast_vote(self):
        if self.radio_bianca.isChecked():
            return 'bianca'
        elif self.radio_edward.isChecked():
            return 'edward'
        elif self.radio_felicia.isChecked():
            return 'felicia'
        else:
            raise Warning


