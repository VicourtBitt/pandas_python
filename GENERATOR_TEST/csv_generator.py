from names_generator import generate_name
from random import random, choice
from datetime import datetime, timedelta

# Função para gerar datas aleatórias  
def gen_datetime(min_year=2020, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return (start + (end - start) * random()).strftime("%d-%m-%Y")

# Função para gerar pagamentos aleatórios, com chance de retornar um valor inválido
def random_payment():
    option = choice(list(range(1, 22)))

    # Provavelmente a forma mais feia de fazer isso, mas funciona
    if option in [n for n in range(1, 21) if n % 2 == 0]:
        return random() * 1000
    elif option in [n for n in range(1, 21) if n % 2 != 0]:
        return random() * 3000
    
    # Adiciona valores inválidos para testar a função isna()
    else:
        return float("nan")

# Função para criar um arquivo CSV com dados de teste
def create_csv(num: int):

    # Abre o arquivo data_sample.csv em modo de escrita
    with open('data_sample.csv', 'w') as file:

        # Escreve o cabeçalho do arquivo
        file.write('id,name,gender,paid,isFiliated,state,date\n')

        # Loop para gerar os dados de teste baseado no número passado como argumento
        for i in range(num):
            userId = i + 1
            name = generate_name(style='capital')
            gender = choice(["Masculino", "Feminino", "Não-binário"])
            paid = random_payment()
            isFiliated = choice([True, False])
            state = choice([
                'RS', 'SC', 'PR', 'SP', 'RJ', 'MG', 'ES', 'MT', 'MS',
                'GO', 'DF', 'BA', 'SE', 'AL', 'PE', 'PB', 'RN', 'CE',
                'PI', 'MA', 'PA', 'AP', 'TO', 'RO', 'AC', 'AM', 'RR'
            ])
            date = gen_datetime()
            # Escreve os dados em cada linha do arquivo
            file.write(f'{userId},{name},{gender},{paid:.2f},{isFiliated},{state},{date}\n')

create_csv(1000)

