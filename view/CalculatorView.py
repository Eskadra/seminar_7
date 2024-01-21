from model.Complex import Complex
class CalculatorView:
    def get_complex_number(self):
        real = float(input("Введите действительную часть комплексного числа: "))
        imaginary = float(input("Введите мнимую часть комплексного числа: "))
        return Complex(real, imaginary)

    def get_operation(self):
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Умножение")
        print("3. Деление")
        choice = int(input("Введите номер операции: "))
        return choice

    def show_result(self, result):
        print("Результат:", result.real, "+", result.imaginary, "i")