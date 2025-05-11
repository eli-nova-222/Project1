from PyQt6.QtWidgets import *
from gui import *
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_submit.clicked.connect(lambda: self.submit())

    def submit(self):
        try:
         id_num = int(self.input_id.text().strip())
         vote = self.cast_vote()

         # writes to csv file
         with open('vote.csv', 'a+', newline='') as csvfile:
             reader = csv.reader(csvfile)
             writer = csv.writer(csvfile)
             vote_data = [id_num, vote]
             writer.writerow(vote_data)

         #reset if correct
         self.label_result.setText('VOTE SUBMITTED')
         self.input_id.setText('')

        #exception for non-int id num
        except ValueError:
            self.label_result.setText(f'ID must only use digits [0-9]')
            self.input_id.setText('')

        except UserWarning:
            self.label_result.setText(f'Please choose a different ID')

            # exception for no candidate selected
        except Warning:
            self.label_result.setText(f'Please select candidate')
            self.input_id.setText('')


    # retrieves button vote
    def cast_vote(self):
        if self.radio_bianca.isChecked():
            return 'bianca'
        elif self.radio_edward.isChecked():
            return 'ed'
        elif self.radio_felicia.isChecked():
            return 'felicia'
        else:
            raise Warning
