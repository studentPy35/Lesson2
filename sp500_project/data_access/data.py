import csv
import json

from .data_errors import (CompanyAlreadyExistsError,
                          NoSuchSymbolError,
                          WrongSectorError)


def provider(file_extension, name):
    if file_extension == '.csv':
        return Sp500Csv(name + file_extension)
    if file_extension == '.json':
        return Sp500Json(name + file_extension)


class FileDB:
    def get_file_information(self):
        return ''

    def check_symbol_uniqueness(self, symbol: str):
        file = self.get_file_information()
        if symbol.lower() in map(lambda dct: dct.get('Symbol').lower(), file):
            raise CompanyAlreadyExistsError('This symbol of'
                                            ' company already exists.')

    def check_symbol_existence(self, symbol):
        file = self.get_file_information()
        if symbol.lower() not in map(lambda dct:
                                     dct.get('Symbol').lower(), file):
            raise NoSuchSymbolError('Company with this symbol is not exist.')

    def check_name_uniqueness(self, name: str):
        file = self.get_file_information()
        if name.lower() in map(lambda dct: dct.get('Name').lower(), file):
            raise CompanyAlreadyExistsError('This company '
                                            'name already exists.')

    def check_sector_existence(self, sector: str):
        file = self.get_file_information()
        if sector.lower() not in map(lambda dct:
                                     dct.get('Sector').lower(), file):
            raise WrongSectorError('This sector is not exist.')


class Sp500Csv(FileDB):
    def __init__(self, file_name):
        self.file_name = file_name

    def get_file_information(self):
        with open(self.file_name, encoding='utf8') as file:
            return list(csv.DictReader(file))

    def record_new_line(self, new_line):
        with open(self.file_name, encoding='utf8') as file:
            headline = csv.DictReader(file).fieldnames
        with open(self.file_name, 'a', encoding='utf8') as new_file:
            writer = csv.DictWriter(new_file, fieldnames=headline)
            writer.writerow(new_line)

    def record_new_information(self, new_information: list):
        with open(self.file_name, encoding='utf8') as file:
            headline = csv.DictReader(file).fieldnames
        with open(self.file_name, 'w', encoding='utf8') as file:
            writer = csv.DictWriter(file, fieldnames=headline)
            writer.writeheader()
            writer.writerows(new_information)


class Sp500Json(FileDB):
    def __init__(self, file_name):
        self.file_name = file_name

    def get_file_information(self):
        with open(self.file_name, encoding='utf8') as file:
            return json.load(file)

    def record_new_line(self, new_line):
        data = self.get_file_information()
        new_info = data.append(new_line)
        with open(self.file_name, 'w', encoding='utf8') as file:
            json.dump(new_info, file, indent=2)

    def record_new_information(self, new_information: list):
        with open(self.file_name, 'w', encoding='utf8') as file:
            json.dump(new_information, file)
