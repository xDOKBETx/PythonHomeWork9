from datetime import datetime


def log_data(text_log):
    folder = r'log_calc.txt'

    with open(folder, 'a+', encoding='UTF-8') as file:
        file.write(f'{datetime.now()}:  {text_log}\n')
