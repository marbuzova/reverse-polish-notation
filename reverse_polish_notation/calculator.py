# Reverse Polish Notation calculator
# Uses stack to evaluate expression
class RPNCalculator:
    type = "RPN"
    number_stack = []
    supported_operands = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    # Evaluate an RPN expression
    def evaluate_expression(self, values):
        tokens = values.split()
        for token in tokens:
            if self.is_supported_operator(token):
                self.number_stack.append(self.perform_operation(token))
            elif self.is_number(token):
                self.number_stack.append(int(token))
                if len(tokens) == 1:
                    return int(token)
            else:
                raise ValueError(
                    "invalid input: %s input must consist of numbers and operators: + - * /"
                    % token
                )

        # last item in stack will be the result
        return self.number_stack[len(self.number_stack) - 1]

    # Check if token is a supported operator: + - * /
    def is_supported_operator(self, token):
        return token in self.supported_operands

    # Check if token consists of digits
    def is_number(self, token):
        return token.lstrip("-+").isdigit()

    # Perform a basic arithmetic operation using +,-,*,/,^
    def perform_operation(self, oper):
        if len(self.number_stack) < 2:
            raise ValueError(
                "invalid input: %s input must be proper RPN expression" % oper
            )
        second = self.number_stack.pop()
        first = self.number_stack.pop()
        return self.supported_operands[oper](first, second)

    # Clears the number stack to start a new operation
    def clear(self):
        self.number_stack = []
