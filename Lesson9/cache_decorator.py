import csv


def find_info(dict_list: list) -> list:
    name = input('Enter the name of company: ')
    company_list = []
    for company_dict in dict_list:
        if name.lower() in company_dict['Name'].lower():
            company_list.append(company_dict)
    return company_list


def get_companies_by_sector(dict_list: list) -> list:
    sector = input('Enter the name of Sector: ')
    return list(filter(lambda comp:
                       sector.lower() == comp['Sector'].lower(), dict_list))


def calculate_average_price(dict_list: list) -> float:
    total_price = 0
    for company_dict in dict_list:
        total_price += float(company_dict['Price'])
    return round(total_price / len(dict_list), 4)


def get_top_10_companies(dict_list: list) -> list:
    sorted_dict_list = sorted(dict_list,
                              key=lambda x: float(x['Price']), reverse=True)
    return [(company_dict['Name'], company_dict['Price'])
            for company_dict in sorted_dict_list[:10]]


def print_goodbye():
    return 'GOODBYE'


print('Choose the action from menu:\n1 - Find info by name\n'
      '2 - Get all companies by sector\n3 - Calculate average price\n'
      '4 - Get top 10 companies\n5 - Exit')


def use_cache(func):
    """Decorator for using cache
    """
    cache_dict = {}

    def wrapper(*args):
        nonlocal cache_dict
        if not cache_dict.get(args):
            result = func(*args)
            cache_dict[args] = result
            return result
        else:
            return cache_dict[args]
        # if args not in cache_dict:
        #     cache_dict[args] = func(*args)
        # return cache_dict
    return wrapper


@use_cache
def get_information(choice_number: str):
    programm = {1: find_info,
                2: get_companies_by_sector,
                3: calculate_average_price,
                4: get_top_10_companies,
                5: print_goodbye}
    with open('sp500.csv', encoding='utf8') as file:
        dict_list_of_companies = list(csv.DictReader(file))
        try:
            if int(choice_number) in range(1, 5):
                return programm[int(choice_number)](dict_list_of_companies)
            else:
                return programm[int(choice_number)]()
        except KeyError:
            return 'You have entered a non-existent ' \
                   'number in the menu. Try again.'
        except ValueError:
            return 'You have to enter a number from menu. Try again.'


print(get_information(input('Your choice: ')))
