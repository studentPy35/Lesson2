from random import uniform, randint
from faker import Faker
from data_access import (get_file_information,
                         record_new_line,
                         record_new_information,
                         check_sector_existence,
                         check_name_uniqueness,
                         check_symbol_uniqueness,
                         check_symbol_existence,
                         CompanyAlreadyExistsError,
                         WrongSectorError,
                         NoSuchSymbolError)
import datetime


def use_cache(live_time=datetime.timedelta(seconds=200)):

    def wrap(func):
        """Decorator for using cache"""
        cache = {}

        def wrapper(*args):
            now = datetime.datetime.now()
            if args not in cache or now - cache[args][0] > live_time:
                value = func(*args)
                cache[args] = (now, value)
            return cache[args][1]
        return wrapper
    return wrap


@use_cache()
def find_info(name: str) -> list:
    company_list = []
    for company_dict in get_file_information():
        if name.lower() in company_dict.get('Name').lower():
            company_list.append(company_dict)
    return company_list


@use_cache()
def get_companies_by_sector(sector: str) -> list:
    return list(filter(lambda comp: sector.lower() == comp['Sector'].lower(),
                       get_file_information()))


def calculate_average_price() -> float:
    total_price = 0
    for company_dict in get_file_information():
        total_price += float(company_dict['Price'])
    return round(total_price / len(get_file_information()), 4)


def get_top_10_companies() -> list:
    sorted_lst = sorted(get_file_information(),
                        key=lambda dct: float(dct['Price']), reverse=True)
    return [(dct['Name'], dct['Price']) for dct in sorted_lst[:10]]


@use_cache()
def add_new_company(symbol: str, name: str, sector: str, price: float):
    try:
        check_symbol_uniqueness(symbol=symbol)
        check_name_uniqueness(name=name)
        check_sector_existence(sector=sector)
        new_line = {'Symbol': symbol,
                    'Name': name,
                    'Sector': sector,
                    'Price': price}
        record_new_line(new_line)
        return True
    except CompanyAlreadyExistsError as err:
        print(err)
    except WrongSectorError as err:
        print(err)


@use_cache()
def update_company_name(symbol: str, name: str):
    try:
        check_symbol_existence(symbol=symbol)
        check_name_uniqueness(name=name)
        file = get_file_information()
        for dct in file:
            if dct.get('Symbol').lower() == symbol.lower():
                dct['Name'] = name
        record_new_information(file)
        return True
    except NoSuchSymbolError as err:
        print(err)
    except CompanyAlreadyExistsError as err:
        print(err)


@use_cache()
def delete_company(symbol: str):
    try:
        check_symbol_existence(symbol=symbol)
        file = get_file_information()
        for dct in file:
            if dct.get('Symbol').lower() == symbol.lower():
                index = file.index(dct)
                del file[index]
        record_new_information(file)
        return True
    except NoSuchSymbolError as err:
        print(err)


def truncate_all():
    file = []
    record_new_information(file)


def take_random_symbol() -> str:
    letters_list = []
    fake = Faker()
    for _ in range(randint(3, 6)):
        letters_list.append(fake.random_uppercase_letter())
    return ''.join(letters_list)


@use_cache()
def generate_random_data(number):
    new_information = []
    fake = Faker()
    for _ in range(int(number)):
        new_information.append({'Symbol': take_random_symbol(),
                                'Price': uniform(0, 1000),
                                'Name': fake.company(),
                                'Sector': fake.catch_phrase()})
    record_new_information(new_information)
