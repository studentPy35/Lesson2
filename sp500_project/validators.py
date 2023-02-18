from errors import (NotDigitError,
                    UnexpectedNumberError,
                    WrongSymbolError,
                    WrongNameLengthError,
                    WrongPriceError,
                    WrongGenerationNumberError)
from string import ascii_uppercase


def validator(choice: str):
    if not choice.isdigit():
        raise NotDigitError('Your choice must be a digit.')
    elif int(choice) not in range(1, 11):
        raise UnexpectedNumberError('Enter a digit from 1 to 5')


def check_symbol(symbol: str):
    if symbol.upper() != symbol:
        raise WrongSymbolError('The letters should be in the upper register.')
    if len(symbol) < 3 or len(symbol) > 6:
        raise WrongSymbolError('The letters length should be from 3 to 6.')
    for letter in symbol:
        if letter not in ascii_uppercase:
            raise WrongSymbolError('The letters should be in ascii')


def check_name(name: str):
    if len(name) < 3 or len(name) > 50:
        raise WrongNameLengthError('The length of company'
                                   ' name should be from 3 to 50.')


def check_price(price: str):
    if float(price) < 0 or float(price) > 1000:
        raise WrongPriceError('The price should be from 0 to 1000.')
    if '.' not in price:
        raise WrongPriceError('The price should be float')


def check_generation_number(number: str):
    if not number.isdigit():
        raise WrongGenerationNumberError('A generation number '
                                         'must be a digit.')
    if int(number) < 0 or int(number) > 10000:
        raise WrongGenerationNumberError('A generation number '
                                         'should be from 0 to 10000.')
