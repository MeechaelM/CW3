import json
from cw3.utils import sorted_operations_status, sorted_operations_date, message


def main():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    data = sorted_operations_status(data)
    data = sorted_operations_date(data)

    for i in range(5):
        print(message(data[i]))
        print()

if __name__ == '__main__':
    main()
