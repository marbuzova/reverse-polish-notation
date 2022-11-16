import sys

from reverse_polish_notation import calculator

rpn_usage_msg = """Reverse Polish Notation calculator 0.1.0 - Bleep, blooop.
Simple RPN calculator using a stack.
Usage:
    > 5 
    5
    > 8
    8
    > +
    13

    > 5 5 5 8 + + -
    -13.0
    > 13 +
    0.0
    
    clear
    0
    
    q
    Exit
"""


# CLI version of calculator
class CommandLine:
    calc = None

    # Supports Reverse Polish Notation evaluation
    def __init__(self, calc_type):
        if calc_type == "RPN":
            self.calc = calculator.RPNCalculator()

    # Runs the CLI
    def start(self):
        self.usage()
        for line in sys.stdin:
            value = line.rstrip()
            if "q" == value:
                break
            if "clear" == value:

                self.calc.clear()
                print(0)
                continue
            try:
                print(f"{self.calc.evaluate_expression(value)}")
            except ValueError as ve:
                print("ValueError: %s" % ve)
            except ZeroDivisionError as zde:
                print("ZeroDivisionError: %s" % zde)
        print("Exit")

    # Prints calculator usage message
    def usage(self):
        if self.calc.type == "RPN":
            print(rpn_usage_msg)
