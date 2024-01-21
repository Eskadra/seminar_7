from model.Complex import Complex
from view.CalculatorView import CalculatorView
class CalculatorController:
    def __init__(self, model, view):
        self.view = view

    def run(self):
        while True:
            complex1 = self.view.get_complex_number()
            complex2 = self.view.get_complex_number()
            operation = self.view.get_operation()

            if operation == 1:
                result = Complex.add(complex1, complex2)
            elif operation == 2:
                result = Complex.multiply(complex1, complex2)
            elif operation == 3:
                result = Complex.divide(complex1, complex2)
            else:
                print("Некорректная операция!")
                continue
            

            self.view.show_result(result)