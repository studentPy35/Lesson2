from random import uniform, randint
from faker import Faker


def find_info(dict_list: list, name: str) -> list:
    company_list = []
    for company_dict in dict_list:
        if name.lower() in company_dict.get('Name').lower():
            company_list.append(company_dict)
    return company_list


def get_companies_by_sector(file: list, sector: str) -> list:
    return list(filter(lambda comp:
                       sector.lower() == comp['Sector'].lower(), file))


def calculate_average_price(file: list) -> float:
    total_price = 0
    for company_dict in file:
        total_price += float(company_dict['Price'])
    return round(total_price / len(file), 4)


def get_top_10_companies(file: list) -> list:
    sorted_lst = sorted(file, key=lambda dct: float(dct['Price']),
                        reverse=True)
    return [(dct['Name'], dct['Price']) for dct in sorted_lst[:10]]


def update_company_name(file: list, symbol: str, name: str) -> list:
    for dct in file:
        if dct.get('Symbol').lower() == symbol.lower():
            dct['Name'] = name
    return file


def delete_company(symbol: str, file: list):
    for dct in file:
        if dct.get('Symbol').lower() == symbol.lower():
            del dct
    return file


def take_random_symbol() -> str:
    letters_list = []
    fake = Faker()
    for _ in range(randint(3, 6)):
        letters_list.append(fake.random_uppercase_letter())
    return ''.join(letters_list)


def generate_random_data(number):
    new_information = []
    fake = Faker()
    for _ in number:
        new_information.append({'Symbol': take_random_symbol(),
                                'Price': uniform(0, 1000),
                                'Name': fake.company(),
                                'Sector': fake.catch_phrase()})
    return new_information
