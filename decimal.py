from typing import Self


class Decimal:
    decimal_number: float

    def __init__(self, decimal_number: float):
        self.decimal_number = decimal_number

    def add(self, number_to_add: Self) -> Self:
        return Decimal(self.decimal_number + number_to_add.decimal_number)

    def is_equal(self, number: Self, precision: int = 2) -> Self:
        return self.to_string(precision) == number.to_string(precision)

    def sub(self, number: Self) -> Self:
        return Decimal(self.decimal_number - number.decimal_number)

    def to_string(self, precision: int = 2):
        return str(round(self.decimal_number, precision))
