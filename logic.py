import csv
from PyQt6.QtWidgets import *
from project2_ui import *


class Logic(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_submit1.clicked.connect(lambda: self.submit())
        self.button_submit2.clicked.connect(lambda: self.submit())
        self.button_submit3.clicked.connect(lambda: self.submit())
        self.button_submit4.clicked.connect(lambda: self.submit())
        self.button_enter.clicked.connect(lambda: self.enter())

        self.__num_attempt = 0
        self.__name = ''

    def submit(self):
        '''
        This function is used for checking the scores entered if they are 0-100
        and if it passes it will make a row of the scores and the top score in the csv file
        '''
        error = False
        if self.__num_attempt == 1:
            try:
                score_1 = int(self.input_score_1.text())
                if 100 < score_1 < 0:
                    raise ValueError
            except:
                self.input_score_1.setText("ERROR(0-100)")
                error = True
            if not error:
                with open("grade_csv.csv", "a",) as grade_csv:
                    csv_writer = csv.writer(grade_csv, lineterminator='\n')
                    csv_writer.writerow([self.__name, score_1, 0, 0, 0, score_1])
                    self.label_submit1.show()
                    self.button_enter.setDisabled(False)

        elif self.__num_attempt == 2:
            try:
                score_1 = int(self.input_score_1.text())
                if 100 < score_1 < 0:
                    raise ValueError
                final_score = score_1
            except:
                self.input_score_1.setText("ERROR(0-100)")
                error = True
            finally:
                try:
                    score_2 = int(self.input_score_2.text())
                    if 100 < score_2 < 0:
                        raise ValueError
                    if final_score < score_2:
                        final_score = score_2
                except:
                    self.input_score_2.setText("ERROR(0-100)")
                    error = True
                if not error:
                    with open("grade_csv.csv", "a",) as grade_csv:
                        csv_writer = csv.writer(grade_csv, lineterminator='\n')
                        csv_writer.writerow([self.__name, score_1, score_2, 0, 0, final_score])
                        self.label_submit2.show()

        elif self.__num_attempt == 3:
            try:
                score_1 = int(self.input_score_1.text())
                if 100 < score_1 < 0:
                    raise ValueError
                final_score = score_1
            except:
                self.input_score_1.setText("ERROR(0-100)")
                error = True
            finally:
                try:
                    score_2 = int(self.input_score_2.text())
                    if 100 < score_2 < 0:
                        raise ValueError
                    if final_score < score_2:
                        final_score = score_2
                except:
                    self.input_score_2.setText("ERROR(0-100)")
                    error = True
                finally:
                    try:
                        score_3 = int(self.input_score_3.text())
                        if 100 < score_3 < 0:
                            raise ValueError
                        if final_score < score_3:
                            final_score = score_3
                    except:
                        self.input_score_3.setText("ERROR(0-100)")
                        error = True
                    if not error:
                        with open("grade_csv.csv", "a",) as grade_csv:
                            csv_writer = csv.writer(grade_csv, lineterminator='\n')
                            csv_writer.writerow([self.__name, score_1, score_2, score_3, 0, final_score])
                            self.label_submit3.show()

        elif self.__num_attempt == 4:
            try:
                score_1 = int(self.input_score_1.text())
                if 100 < score_1 < 0:
                    raise ValueError
                final_score = score_1
            except:
                self.input_score_1.setText("ERROR(0-100)")
                error = True
            finally:
                try:
                    score_2 = int(self.input_score_2.text())
                    if 100 < score_2 < 0:
                        raise ValueError
                    if final_score < score_2:
                        final_score = score_2
                except:
                    self.input_score_2.setText("ERROR(0-100)")
                    error = True
                finally:
                    try:
                        score_3 = int(self.input_score_3.text())
                        if 100 < score_3 < 0:
                            raise ValueError
                        if final_score < score_3:
                            final_score = score_3
                    except:
                        self.input_score_3.setText("ERROR(0-100)")
                        error = True
                    finally:
                        try:
                            score_4 = int(self.input_score_4.text())
                            if 100 < score_4 < 0:
                                raise ValueError
                            if final_score < score_4:
                                final_score = score_4
                        except:
                            self.input_score_4.setText("ERROR(0-100)")
                            error = True
                        if not error:
                            with open("grade_csv.csv", "a") as grade_csv:
                                csv_writer = csv.writer(grade_csv, lineterminator='\n')
                                csv_writer.writerow([self.__name, score_1, score_2, score_3, score_4, final_score])
                                self.label_submit4.show()


    def enter(self):
        '''
        This function is used to check if the name entered is in the csv file already and check the input for
        attempts making sure it is 1-4 then depending on the number will adjust
        the window and show the score input boxes and submit button
        '''
        self.__name = self.input_name.text()
        with open('grade_csv.csv', 'r') as grade_csv:
            csv_reader = csv.reader(grade_csv)
            next(csv_reader)
            try:
                for row in csv_reader:
                    if self.__name == row[0]:
                        raise ValueError
            except ValueError:
                self.input_name.setText('STUDENT ALREADY EXISTS')
                return None
            finally:
                try:
                    self.__num_attempt = int(self.input_attempts.text())
                    if self.__num_attempt < 1 or self.__num_attempt > 4:
                        raise TypeError
                except:
                    self.input_attempts.setText('INPUT A VALID NUMBER(1-4)')
                    return None
        if self.__num_attempt == 1:
            self.setFixedHeight(259)
            self.centralwidget.setFixedHeight(259)
            self.label_score_1.show()
            self.input_score_1.show()
            self.button_submit1.show()

        elif self.__num_attempt == 2:
            self.setFixedHeight(308)
            self.centralwidget.setFixedHeight(308)
            self.label_score_1.show()
            self.input_score_1.show()
            self.label_score_2.show()
            self.input_score_2.show()
            self.button_submit2.show()

        elif self.__num_attempt == 3:
            self.setFixedHeight(358)
            self.centralwidget.setFixedHeight(358)
            self.label_score_1.show()
            self.input_score_1.show()
            self.label_score_2.show()
            self.input_score_2.show()
            self.label_score_3.show()
            self.input_score_3.show()
            self.button_submit3.show()

        elif self.__num_attempt == 4:
            self.setFixedHeight(413)
            self.centralwidget.setFixedHeight(413)
            self.label_score_1.show()
            self.input_score_1.show()
            self.label_score_2.show()
            self.input_score_2.show()
            self.label_score_3.show()
            self.input_score_3.show()
            self.label_score_4.show()
            self.input_score_4.show()
            self.button_submit4.show()
        self.button_enter.setDisabled(True)
