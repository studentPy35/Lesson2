import csv

from .data_errors import (CompanyAlreadyExistsError,
                          NoSuchSymbolError,
                          WrongSectorError)


def get_file_information() -> list:
    with open('sp500.csv', encoding='utf8') as file:
        return list(csv.DictReader(file))


def record_new_line(new_line):
    with open('sp500.csv', encoding='utf8') as file:
        headline = csv.DictReader(file).fieldnames
    with open('sp500.csv', 'a', encoding='utf8') as new_file:
        writer = csv.DictWriter(new_file, fieldnames=headline)
        writer.writerow(new_line)


def record_new_information(new_information: list):
    with open('sp500.csv', encoding='utf8') as file:
        headline = csv.DictReader(file).fieldnames
    with open('sp500.csv', 'w', encoding='utf8') as file:
        writer = csv.DictWriter(file, fieldnames=headline)
        writer.writeheader()
        writer.writerows(new_information)


def check_symbol_uniqueness(symbol: str):
    file = get_file_information()
    if symbol.lower() in map(lambda dct: dct.get('Symbol').lower(), file):
        raise CompanyAlreadyExistsError('This symbol of'
                                        ' company already exists.')


def check_symbol_existence(symbol):
    file = get_file_information()
    if symbol.lower() not in map(lambda dct: dct.get('Symbol').lower(), file):
        raise NoSuchSymbolError('Company with this symbol is not exist.')


def check_name_uniqueness(name: str):
    file = get_file_information()
    if name.lower() in map(lambda dct: dct.get('Name').lower(), file):
        raise CompanyAlreadyExistsError('This company name already exists.')


def check_sector_existence(sector: str):
    file = get_file_information()
    if sector.lower() not in map(lambda dct: dct.get('Sector').lower(), file):
        raise WrongSectorError('This sector is not exist.')
