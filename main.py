import sys

from PyQt5 import QtWidgets
import math

from calci_ui import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_widget.setVisible(False)

        ### Page Connect
        self.ui.std_Pbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.Sci_Pbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.DateC_PBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.Curr_PBtn.clicked.connect(lambda checked, show_frame=0: self.show_conv_Page(show_frame))
        self.ui.leng_Pbtn.clicked.connect(lambda checked, show_frame=1: self.show_conv_Page(show_frame))
        self.ui.Tem_Pbtn.clicked.connect(lambda checked, show_frame=2: self.show_conv_Page(show_frame))
        self.ui.Time_Pbtn.clicked.connect(lambda checked, show_frame=3: self.show_conv_Page(show_frame))
        self.ui.Speed_Pbtn.clicked.connect(lambda checked, show_frame=4: self.show_conv_Page(show_frame))
        self.ui.Weight_Pbtn.clicked.connect(lambda checked, show_frame=5: self.show_conv_Page(show_frame))

        ### Standard Page Functions
        self.ui.zero_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '0'))
        self.ui.one_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '1'))
        self.ui.two_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '2'))
        self.ui.three_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '3'))
        self.ui.four_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '4'))
        self.ui.five_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '5'))
        self.ui.six_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '6'))
        self.ui.seven_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '7'))
        self.ui.eightpbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '8'))
        self.ui.nine_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '9'))

        self.ui.dot_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '.'))
        self.ui.c_pbtn.clicked.connect(lambda : self.ui.std_out_label.setText(''))
        self.ui.back_pbtn.clicked.connect(self.back_label_fun)
        self.ui.signch_pbtn.clicked.connect(self.change_sign)

        self.ui.add_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '+'))
        self.ui.sub_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '-'))
        self.ui.mul_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '*'))
        self.ui.divi_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '/'))
        self.ui.mod_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '%'))
        self.ui.uponX_pbtn.clicked.connect(self.uponx_function)
        self.ui.x_square_pbtn.clicked.connect(self.x_square_fun)
        self.ui.x_sqrt_pbtn.clicked.connect(self.x_sqrt_fun)
        self.ui.ce_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '2.718'))
        self.ui.equal_pbtn.clicked.connect(self.evaluate_expr)


        ### Scientific Page Function
        self.ui.zero_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '0'))
        self.ui.one_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '1'))
        self.ui.two_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '2'))
        self.ui.three_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '3'))
        self.ui.four_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '4'))
        self.ui.five_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '5'))
        self.ui.six_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '6'))
        self.ui.seven_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '7'))
        self.ui.eightpbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '8'))
        self.ui.nine_pbtn.clicked.connect(lambda: self.ui.std_out_label.setText(self.ui.std_out_label.text() + '9'))

        ### Date Calculation Page Function
        self.ui.find_date_diff_pbtn.clicked.connect(self.date_difference)

        ### Convertor Page
        self.ui.convert_pbtn.clicked.connect(self.call_convert_fun)

    def evaluate_expr(self):
        try:
            expression = self.ui.std_out_label.text()
            index = expression.find("√")
            if index >=0:
                modified_string = expression[:index] + "math.sqrt" + expression[index + 1:]
            else:
                modified_string =expression
            result = eval(modified_string)
            self.ui.std_out_label.setText(str(result))
        except Exception as e:
            print(f"An error occurred: {e}")
            return


    def uponx_function(self):
        expression = self.ui.std_out_label.text()
        if not expression:
            return
        last_number = expression.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1].split("%")[-1]
        expression = expression[:-len(last_number)] + "(1/(" +last_number +"))"
        self.ui.std_out_label.setText(expression)

    def x_square_fun(self):
        expression = self.ui.std_out_label.text()
        if not expression:
            return
        last_number = expression.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1].split("%")[-1]
        expression = expression[:-len(last_number)] + last_number + "**2"
        self.ui.std_out_label.setText(expression)

    def x_sqrt_fun(self):
        expression = self.ui.std_out_label.text()
        if not expression:
            return
        last_number = expression.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1].split("%")[-1]
        expression = expression[:-len(last_number)] +  "√(" + last_number + ")"
        self.ui.std_out_label.setText(expression)

    def change_sign(self):
        try:
            expression = self.ui.std_out_label.text()
            if not expression:
                return
            last_number = expression.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1]
            if last_number and last_number[0] == "-":
                expression = expression[:-len(last_number)] + last_number[1:]
            else:
                expression = expression[:-len(last_number)] + "-" + last_number
            self.ui.std_out_label.setText(expression)
        except Exception as e:
            print(f"An error occurred: {e}")
            return
    def back_label_fun(self):
        current_text = self.ui.std_out_label.text()
        new_text = current_text[:-1]
        self.ui.std_out_label.setText(new_text)

    def show_conv_Page(self, state):
        try:
            if state == 0:
                self.conversion_factors = {
                    "USD": 1.0,
                    "EUR": 0.85,
                    "GBP": 0.74,
                    "JPY": 110.49,
                    "INR": 73.67,
                }
                self.ui.label_2.setText("Currency Convertor")
            elif state == 1:
                self.conversion_factors = {
                    "Meters": 1.0,
                    "Kilometers": 0.001,
                    "Feet": 3.28084,
                    "Inches": 39.3701,
                    "Centimeters": 100.0,
                }
                self.ui.label_2.setText("Length Convertor")
            elif state == 2:
                self.conversion_factors = {
                    "Celsius": {"Celsius": 1.0, "Fahrenheit": 1.8, "Kelvin": 1.0},
                    "Fahrenheit": {"Celsius": 5 / 9, "Fahrenheit": 1.0, "Kelvin": 5 / 9},
                    "Kelvin": {"Celsius": 1.0, "Fahrenheit": 1.8, "Kelvin": 1.0},
                }
                self.ui.label_2.setText("Temperature Convertor")
            elif state == 3:
                self.conversion_factors = {
                    "Hours": {"Hours": 1.0, "Minutes": 60.0, "Seconds": 3600.0},
                    "Minutes": {"Hours": 1 / 60.0, "Minutes": 1.0, "Seconds": 60.0},
                    "Seconds": {"Hours": 1 / 3600.0, "Minutes": 1 / 60.0, "Seconds": 1.0},
                }
                self.ui.label_2.setText("Time Convertor")
            elif state == 4:
                self.conversion_factors = {
                    "m/s": {"m/s": 1.0, "km/h": 3.6, "mph": 2.23694},
                    "km/h": {"m/s": 0.277778, "km/h": 1.0, "mph": 0.621371},
                    "mph": {"m/s": 0.44704, "km/h": 1.60934, "mph": 1.0},
                }
                self.ui.label_2.setText("Speed Convertor")
            else:
                self.conversion_factors = {
                    "Kilograms": {"Kilograms": 1.0, "Grams": 1000.0, "Pounds": 2.20462},
                    "Grams": {"Kilograms": 0.001, "Grams": 1.0, "Pounds": 0.00220462},
                    "Pounds": {"Kilograms": 0.453592, "Grams": 453.592, "Pounds": 1.0},
                }
                self.ui.label_2.setText("Weight Convertor")
            self.ui.from_con_combobox.addItems(list(self.conversion_factors.keys()))
            self.ui.to_con_combobox.addItems(list(self.conversion_factors.keys()))
            self.ui.stackedWidget.setCurrentIndex(3)
        except Exception as e:
            print(f"An error occurred: {e}")


    def convert_curr_len(self):
        try:
            value = float(self.ui.lineEdit.text())
            from_curr = self.ui.from_con_combobox.currentText()
            to_curr = self.ui.to_con_combobox.currentText()
            converted_value = value * self.conversion_factors[to_curr] / self.conversion_factors[from_curr]
            self.ui.label_4.setText(f"{converted_value:.2f} {to_curr}")
        except ValueError:
            self.ui.label_4.setText("Invalid input")

    def convert_tem_time_speed_wei(self):
        try:
            value = float(self.ui.lineEdit.text())
            from_unit = self.ui.from_con_combobox.currentText()
            to_unit = self.ui.to_con_combobox.currentText()
            converted_value = value * self.conversion_factors[from_unit][to_unit]
            self.ui.label_4.setText(f"{converted_value:.2f} {to_unit}")
        except ValueError:
            self.ui.label_4.setText("Invalid input")

    def call_convert_fun(self):
        try:
            if self.ui.label_2.text() == "Currency Convertor" or self.ui.label_2.text() == "Length Convertor":
                self.convert_curr_len()
            else:
                self.convert_tem_time_speed_wei()
        except Exception as e:
            print(f"An error occurred: {e}")

    def date_difference(self):
        try:
            start_date = self.ui.from_dEdit.date()
            end_date = self.ui.to_dEdit.date()
            difference = start_date.daysTo(end_date)
            years = difference // 365
            remaining_days = difference % 365
            months = remaining_days // 30
            days = remaining_days % 30
            result = f"Date Difference: {years} years, {months} months, {days} days"
            self.ui.date_diff_out.setText(result)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())