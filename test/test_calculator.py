import unittest

from reverse_polish_notation.calculator import RPNCalculator


class RPNCalculatorTest(unittest.TestCase):
    # set up the environment needed for the test
    def setUp(self):
        self.calc = RPNCalculator()
        self.calc.clear()

    def test_evaluate_expression__expression(self):
        self.assertEqual(self.calc.evaluate_expression("5 5 5 8 + + -"), -13.0)

    def test_evaluate_expression__single_value(self):
        result = self.calc.evaluate_expression("1")
        self.assertEqual(result, 1)
        result = self.calc.evaluate_expression("2")
        self.assertEqual(result, 1)
        result = self.calc.evaluate_expression("+")
        self.assertEqual(result, 3.0)

    def test_evaluate_expression__mixed(self):
        self.assertEqual(self.calc.evaluate_expression("5 5 5 8 + + -"), -13.0)
        self.assertEqual(self.calc.evaluate_expression("13 +"), 0.0)

    def test_evaluate_expression__unsupported_operation(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate_expression("5 5 ^")

    def test_evaluate_expression__non_number(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate_expression("a")

    def test_perform_operation__plus(self):
        self.calc.number_stack = [3, 2]
        self.assertEqual(self.calc.perform_operation("+"), 5)

    def test_perform_operation__minus(self):
        self.calc.number_stack = [3, 2]
        self.assertEqual(self.calc.perform_operation("-"), 1)

    def test_perform_operation__mult(self):
        self.calc.number_stack = [3, 2]
        self.assertEqual(self.calc.perform_operation("*"), 6)

    def test_perform_operation__divide(self):
        self.calc.number_stack = [3, 2]
        self.assertEqual(self.calc.perform_operation("/"), 1.5)

    def test_perform_operation__empty_stack(self):
        self.calc.number_stack = []
        with self.assertRaises(ValueError):
            self.calc.perform_operation("+")

    def test_is_number(self):
        self.assertEqual(self.calc.is_number("10"), True)
        self.assertEqual(self.calc.is_number("-10"), True)
        self.assertEqual(self.calc.is_number("a"), False)
        self.assertEqual(self.calc.is_number("+"), False)

    def test_is_supported_operator(self):
        self.assertEqual(self.calc.is_supported_operator("+"), True)
        self.assertEqual(self.calc.is_supported_operator("-"), True)
        self.assertEqual(self.calc.is_supported_operator("*"), True)
        self.assertEqual(self.calc.is_supported_operator("/"), True)
        self.assertEqual(self.calc.is_supported_operator("^"), False)

    def test_clear(self):
        self.calc.number_stack = [1, 2, 3]
        self.calc.clear()
        self.assertEqual(self.calc.number_stack, [])
