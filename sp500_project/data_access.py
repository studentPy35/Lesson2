import csv


def get_file_information() -> list:
    with open('sp500.csv', encoding='utf8') as file:
        return list(csv.DictReader(file))


def headliners():
    with open('sp500.csv', encoding='utf8') as file:
        return csv.DictReader(file).fieldnames


def add_new_line(symbol: str, name: str, sector: str, price: float):
    with open('sp500.csv', 'a', encoding='utf8') as file:
        writer = csv.DictWriter(file, fieldnames=headliners())
        writer.writerow({'Symbol': symbol,
                         'Name': name,
                         'Sector': sector,
                         'Price': price})


def change_file_information(new_information: list):
    with open('sp500.csv', 'w', encoding='utf8') as file:
        writer = csv.DictWriter(file, fieldnames=headliners())
        writer.writerows(new_information)


def truncate_all():
    with open('sp500.csv', 'r+', encoding='utf8') as file:
        file.truncate()
