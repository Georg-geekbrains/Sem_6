
import argparse

def _is_leap_year(year):
    
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def validate_date(date_str):
    
    day, month, year = map(int, date_str.split('.'))

    if year < 1 or year > 9999:
        return False

    if month < 1 or month > 12:
        return False

    if day < 1:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:  
        if day > 31:
            return False
    elif month in [4, 6, 9, 11]:  
        if day > 30:
            return False
    else:  
        if _is_leap_year(year):  
            if day > 29:
                return False
        else:
            if day > 28:
                return False

    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Проверка корректности даты.')
    parser.add_argument('date', type=str, help='Дата в формате DD.MM.YYYY')
    args = parser.parse_args()

    if validate_date(args.date):
        print("Дата корректна.")
    else:
        print("Дата некорректна.")

