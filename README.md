<div align="center">

# Reverse Polish Notation Calculator

A simple calculator supporting Reverse Polish Notation calculation. 

</div>

## Overview
This is a Python implementation of command-line reverse polish notation (RPN) calculator.
It supports the four basic arithmetic operations of +, -, *, /, and can be extended for
other operators. 

Reverse Polish Notation is postfix notation which in terms of mathematical notion
signifies operators following operands.

Commands:
* clear - to clear result
* q - to exit

Example input:
```bash
~ % reverse-polish
Reverse Polish Notation calculator 0.1.0 - Bleep, blooop.
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
```

## Install

```bash
# Install tool
pip3 install reverse_polish_notation

# Install locally
make install
```

## Running

```bash
# Option one
venv/bin/python reverse_polish_notation/app.py

# Option two
reverse-polish 
```

## Development

```bash
# Get a comprehensive list of development tools
make help
```

## Tests

```bash
# Run all tests
make test

# Get code coverage
make coverage
```

## Solution
The approach of this solution uses a stack for keeping track of remaining operands and result.

We evaluate the RPN expression as following:
1. For every item in the input array, 
   a. if a number, push to the stack. 
   b. if an operator, pop the first two numbers from stack, perform operation, and push the result to the stack.
2. Return the first element of the stack

Time complexity: O(n)
Space complexity: O(n)
Since we visit each item in input array, and they may all be numbers, 
our auxilary space will be at most size of the input, n. 

## Future improvements
With larger scope of production-readying, extra additions would be:
* tests for command-line functionality
* logger
* environment specific configurations
* change log
* scripts/packaging to deploy

## Helpful Links
* [About Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
* [Infix to RPN/Postfix converter](https://www.mathblog.dk/tools/infix-postfix-converter/) 
* [Original Problem Prompt](https://gist.github.com/dennisbaskin/5979ff6a0d8c1e90b59d060155862767)
