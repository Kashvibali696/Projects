from __future__ import unicode_literals


def validate_credit_card_number(card_number):
    card_number = str(card_number)
    if not card_number.isdigit():
        raise Exception('Not a valid number')

    card_number = [int(digit) for digit in card_number if digit.isdigit()]
    base_card_number = list(reversed(card_number[:-1]))
    for index, digit in enumerate(base_card_number):
        if (index + 1) % 2 != 0:
            base_card_number[index] = digit * 2
        if base_card_number[index] > 9:
            base_card_number[index] -= 9
    print sum(base_card_number)
    return sum(base_card_number) % 10 == 0
