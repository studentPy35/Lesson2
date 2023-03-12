from random import uniform, randint
from faker import Faker
from data_access import (CompanyAlreadyExistsError,
                         WrongSectorError,
                         NoSuchSymbolError,
                         provider)
from time import time
from config import file_extension, name_of_db

cache = {}


def use_cache(live_time=10):
    def wrap(func):
        """Decorator for using cache"""

        def wrapper(*args, **kwargs):
            now = time()
            if args not in cache or now - cache[args][0] > live_time:
                value = func(*args, **kwargs)
                cache[args] = (now, value)
            return cache[args][1]

        return wrapper

    return wrap


@use_cache()
def find_info(text: str) -> list:
    company_list = []
    for company_dict in provider(file_extension,
                                 name_of_db).get_file_information():
        if text.lower() in company_dict.get('Name').lower():
            company_list.append(company_dict)
    return company_list


@use_cache()
def get_companies_by_sector(sector: str) -> list:
    return list(filter(lambda comp: sector.lower() == comp['Sector'].lower(),
                       provider(file_extension,
                                name_of_db).get_file_information()))


def calculate_average_price() -> float:
    total_price = 0
    for company_dict in provider(file_extension,
                                 name_of_db).get_file_information():
        total_price += float(company_dict['Price'])
    return round(total_price /
                 len(provider(file_extension,
                              name_of_db).get_file_information()), 4)


def get_top_10_companies() -> list:
    sorted_lst = sorted(provider(file_extension,
                                 name_of_db).get_file_information(),
                        key=lambda dct: float(dct['Price']), reverse=True)
    return [(dct['Name'], dct['Price']) for dct in sorted_lst[:10]]


@use_cache()
def add_new_company(symbol: str, new_name: str, sector: str, price: float):
    try:
        provider(file_extension,
                 name_of_db).check_symbol_uniqueness(symbol=symbol)
        provider(file_extension,
                 name_of_db).check_name_uniqueness(name=new_name)
        provider(file_extension,
                 name_of_db).check_sector_existence(sector=sector)
        new_line = {'Symbol': symbol,
                    'Name': new_name,
                    'Sector': sector,
                    'Price': price}
        provider(file_extension, name_of_db).record_new_line(new_line)
        return True
    except CompanyAlreadyExistsError as err:
        print(err)
    except WrongSectorError as err:
        print(err)


@use_cache()
def update_company_name(symbol: str, new_name: str):
    try:
        provider(file_extension,
                 name_of_db).check_symbol_existence(symbol=symbol)
        provider(file_extension,
                 name_of_db).check_name_uniqueness(name=new_name)
        file = provider(file_extension,
                        name_of_db).get_file_information()
        for dct in file:
            if dct.get('Symbol').lower() == symbol.lower():
                dct['Name'] = new_name
        provider(file_extension,
                 name_of_db).record_new_information(file)
        return True
    except NoSuchSymbolError as err:
        print(err)
    except CompanyAlreadyExistsError as err:
        print(err)


@use_cache()
def delete_company(symbol: str):
    try:
        provider(file_extension,
                 name_of_db).check_symbol_existence(symbol=symbol)
        file = provider(file_extension,
                        name_of_db).get_file_information()
        for dct in file:
            if dct.get('Symbol').lower() == symbol.lower():
                index = file.index(dct)
                del file[index]
        provider(file_extension,
                 name_of_db).record_new_information(file)
        return True
    except NoSuchSymbolError as err:
        print(err)


def truncate_all():
    file = []
    provider(file_extension, name_of_db).record_new_information(file)


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
    provider(file_extension,
             name_of_db).record_new_information(new_information)
