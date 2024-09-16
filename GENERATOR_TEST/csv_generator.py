from names_generator import generate_name
from random import random, choice
from datetime import datetime, timedelta

# money = (random() * 1000) + 1
# state = choice(stateArray)
# stateArray = [
#     'RS', 'SC', 'PR', 'SP', 'RJ', 'MG', 'ES', 'MT', 'MS',
#     'GO', 'DF', 'BA', 'SE', 'AL', 'PE', 'PB', 'RN', 'CE',
#     'PI', 'MA', 'PA', 'AP', 'TO', 'RO', 'AC', 'AM', 'RR'
# ]

def gen_datetime(min_year=2020, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return (start + (end - start) * random()).strftime("%d-%m-%Y")

def create_csv(num: int):
    with open('data_sample.csv', 'w') as file:

        file.write('id,name,paid,isFiliated,state,date\n')

        for i in range(num):
            userId = i
            name = generate_name(style='capital')
            paid = ((random() * 1000) + 1)
            isFiliated = choice([True, False])
            state = choice([
                'RS', 'SC', 'PR', 'SP', 'RJ', 'MG', 'ES', 'MT', 'MS',
                'GO', 'DF', 'BA', 'SE', 'AL', 'PE', 'PB', 'RN', 'CE',
                'PI', 'MA', 'PA', 'AP', 'TO', 'RO', 'AC', 'AM', 'RR'
            ])
            date = gen_datetime()
            file.write(f'{userId},{name},{paid:.2f},{isFiliated},{state},{date}\n')

create_csv(1000)