from model.Complex import Complex
from view.CalculatorView import CalculatorView
from controller.CalculatorController import CalculatorController
import logging


def main():
    logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    model = Complex(0,0)
    view = CalculatorView()
    controller = CalculatorController(model, view)
    controller.run()

if __name__ == "__main__":
    main()