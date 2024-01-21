import logging
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        logging.info(f'add real: {self.real} + {other.real} | add imaginary: {self.imaginary} + {other.imaginary} |Result: {new_real} + {new_imaginary} i')
        return Complex(new_real, new_imaginary)

    def multiply(self, other):
        new_real = self.real * other.real - self.imaginary * other.imaginary
        new_imaginary = self.real * other.imaginary + self.imaginary * other.real
        logging.info(f'multiply real: {self.real} * {other.real} - {self.imaginary} * {other.imaginary} | multiply imaginary: {self.real} * {other.imaginary} + {self.imaginary} * {other.real} | Result: {new_real} + {new_imaginary} i')
        return Complex(new_real, new_imaginary)

    def divide(self, other):
        denominator = other.real * other.real + other.imaginary * other.imaginary
        new_real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        new_imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        logging.info(f'divide real: ({self.real} * {other.real} + {self.imaginary} * {other.imaginary}) / {denominator} | divide imaginary: ({self.imaginary} * {other.real} - {self.real} * {other.imaginary}) / {denominator} | Result: {new_real} + {new_imaginary} i')
        return Complex(new_real, new_imaginary)