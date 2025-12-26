"""
calculator.py

A small, clean module demonstrating pylint-compliant Python code.
"""

from typing import Union


Number = Union[int, float]


def add(first: Number, second: Number) -> Number:
    """
    Add two numbers and return the result.

    :param first: First numeric value
    :param second: Second numeric value
    :return: Sum of both values
    """
    return first + second


def subtract(first: Number, second: Number) -> Number:mfd
    """
    Subtract the second number from the first.

    :param first: First numeric value
    :param second: Second numeric value
    :return: Difference of both values
    """
    return first - second


def main() -> None:
    """
    Main execution function.
    """
    value_one: Number = float(input("Enter the first number: "))
    value_two: Number = float(input("Enter the  second number: "))

    total: Number = add(value_one, value_two)
    difference: Number = subtract(value_one, value_two)

    print(f"Addition result: {total}")
    print(f"Subtraction result: {difference}")


if __name__ == "__main__":
    main()
