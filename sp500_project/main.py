from data_access import (get_file_information,
                         add_new_line,
                         change_file_information,
                         truncate_all)
from business_logic import (find_info,
                            get_companies_by_sector,
                            calculate_average_price,
                            get_top_10_companies,
                            update_company_name,
                            delete_company,
                            generate_random_data)
from validators import (validator,
                        check_name,
                        check_price,
                        check_sector,
                        check_symbol,
                        check_name_uniqueness,
                        check_symbol_uniqueness,
                        check_symbol_existence,
                        check_generation_number)
from errors import (NotDigitError,
                    UnexpectedNumberError,
                    WrongSymbolError,
                    CompanyAlreadyExistsError,
                    WrongNameLengthError,
                    WrongSectorError,
                    WrongPriceError,
                    NoSuchSymbolError,
                    WrongGenerationNumberError)


while True:
    choice = input('Choose the action from menu:\n'
                   '1 - Find info by name\n'
                   '2 - Get all companies by sector\n'
                   '3 - Calculate average price\n'
                   '4 - Get top 10 companies\n'
                   '5 - Exit\n'
                   '6 - Add new company\n'
                   '7 - Update company name\n'
                   '8 - Delete company\n'
                   '9 - Truncate all\n'
                   '10 - Populate file with random data\n'
                   'Your choice: '
                   )
    try:
        validator(choice)
    except NotDigitError as err:
        print(err)
        continue
    except UnexpectedNumberError as err:
        print(err)
        continue

    if int(choice) == 1:
        name = input('Enter the name of company: ')
        print(find_info(get_file_information(), name))
    elif int(choice) == 2:
        sector = input('Enter the name of Sector: ')
        print(get_companies_by_sector(get_file_information(), sector))
    elif int(choice) == 3:
        print(calculate_average_price(get_file_information()))
    elif int(choice) == 4:
        print(get_top_10_companies(get_file_information()))
    elif int(choice) == 5:
        print('GOODBYE')
        break
    elif int(choice) == 6:
        symbol = input('Enter the symbol of company: ')
        try:
            check_symbol(symbol=symbol)
            check_symbol_uniqueness(symbol=symbol, file=get_file_information())
        except WrongSymbolError as err:
            print(err)
            continue
        except CompanyAlreadyExistsError as err:
            print(err)
            continue

        sector = input('Enter the Sector: ')
        try:
            check_sector(sector=sector, file=get_file_information())
        except WrongSectorError as err:
            print(err)
            continue

        name = input('Enter the name of company: ')
        try:
            check_name(name=name)
            check_name_uniqueness(name=name, file=get_file_information())
        except WrongNameLengthError as err:
            print(err)
            continue
        except CompanyAlreadyExistsError as err:
            print(err)
            continue

        price = input('Enter the price: ')
        try:
            check_price(price=price)
        except WrongPriceError as err:
            print(err)
            continue

        add_new_line(symbol=symbol, name=name, price=float(price),
                     sector=sector)
        print('The new company has added')

    elif int(choice) == 7:
        symbol = input('Enter the symbol of company: ')
        try:
            check_symbol_existence(symbol=symbol, file=get_file_information())
        except NoSuchSymbolError as err:
            print(err)
            continue

        name = input('Enter a new name of company: ')
        try:
            check_name_uniqueness(name=name, file=get_file_information())
            check_name(name=name)
        except CompanyAlreadyExistsError as err:
            print(err)
            continue
        except WrongNameLengthError as err:
            print(err)
            continue

        change_file_information(update_company_name(get_file_information(),
                                symbol,
                                name))

    elif int(choice) == 8:
        symbol = input('Enter the symbol of company: ')
        try:
            check_symbol_existence(symbol=symbol, file=get_file_information())
        except NoSuchSymbolError as err:
            print(err)
            continue

        change_file_information(delete_company(symbol=symbol,
                                               file=get_file_information()))

    elif int(choice) == 9:
        truncate_all()

    elif int(choice) == 10:
        records_number = input('Enter a number of records for generation: ')
        try:
            check_generation_number(number=records_number)
        except WrongGenerationNumberError as err:
            print(err)
            continue

        change_file_information(generate_random_data(records_number))
