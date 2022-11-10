from cgitb import text
import breaking_data as bd
import check as ch


def math_complex_number(data: str):
    def math_operations(list_data: list):

        while True:
            try:
                float(list_data[0][0])
                float(list_data[0][1])
                if len(list_data) > 1 and list_data.count('*') == 0 and list_data.count('/') == 0 and list_data.count(
                        '+') == 0 and list_data.count('-') == 0:
                    err = 'no signs'
                    return ch.alarm_check(str(err))

                if list_data.count('*') > 0 or list_data.count('/') > 0:
                    if list_data.count('*') > 0 and list_data.count('/') > 0 and (
                            list_data.index('*') < list_data.index('/')):
                        attr = '*'
                    elif list_data.count('*') > 0 and list_data.count('/') > 0 and (
                            list_data.index('/') < list_data.index('+')):
                        attr = '/'
                    elif list_data.count('*') > 0:
                        attr = '*'
                    else:
                        attr = '/'
                elif list_data.count('+') > 0 or list_data.count('-') > 0:
                    if list_data.count('+') > 0 and list_data.count('-') > 0 and (
                            list_data.index('+') < list_data.index('-')):
                        attr = '+'
                    elif list_data.count('-') > 0 and list_data.count('+') > 0 and (
                            list_data.index('-') < list_data.index('+')):
                        attr = '-'
                    elif list_data.count('+') > 0:
                        attr = '+'
                    else:
                        attr = '-'
                else:
                    break

                index_attribute = list_data.index(attr)
                a = float(list_data[index_attribute - 1][0])
                b = float(list_data[index_attribute - 1][1])
                c = float(list_data[index_attribute + 1][0])
                d = float(list_data[index_attribute + 1][1])
                if attr == '*':
                    temp_number1 = a * c - b * d
                    temp_number2 = b * c + a * d
                elif attr == '/':
                    temp_number1 = (a * c - b * d) / (c ** 2 + d ** 2)
                    temp_number2 = (b * c - a * d) / (c ** 2 + d ** 2)
                elif attr == '+':
                    temp_number1 = a + c
                    temp_number2 = b + d
                elif attr == '-':
                    temp_number1 = a - c
                    temp_number2 = b - d
                temp_number = [str(temp_number1), str(temp_number2)]
            except (ZeroDivisionError, ValueError, IndexError) as err:
                return ch.alarm_check(str(err))

            for _ in range(3):
                list_data.pop(index_attribute - 1)

            list_data.insert(index_attribute - 1, temp_number)

        return False, '', list_data[0]

    def quotes_math(list_number_attributes: list):

        while list_number_attributes.count('(') > 0:
            try:
                index_el_1 = -1
                index_el_2 = -1

                for i, x in enumerate(list_number_attributes):
                    if x == '(':
                        index_el_1 = i
                    if x == ')' and index_el_1 != -1:
                        index_el_2 = i
                        break

                new_list_number = []

                new_list_number = [list_number_attributes[ind] for ind in range(index_el_1 + 1, index_el_2)]

                bool_error, text_error, temp_number = math_operations(new_list_number)
                if bool_error == True:
                    return bool_error, text_error, temp_number

                for _ in range(index_el_2 - index_el_1 + 1):
                    list_number_attributes.pop(index_el_1)

                list_number_attributes.insert(index_el_1, temp_number)

                new_list_number.clear()
            except (ZeroDivisionError, ValueError, IndexError) as err:
                return ch.alarm_check(str(err))

        return math_operations(list_number_attributes)

    bool_error, text_error, list_data_number = bd.breaking_complex_data(data)

    if bool_error == False:
        bool_error, text_error, number = quotes_math(list_data_number)

    if bool_error == False:
        if float(number[0]) != 0 and float(number[1]) > 0:
            complex_str = f'({number[0]}+{str(float(number[1]))}i)'
        elif float(number[0]) != 0 and float(number[1]) < 0:
            complex_str = f'({number[0]}{number[1]}i)'
        elif float(number[0]) == 0:
            complex_str = f'{number[1]}i'
        else:
            complex_str = '0'
    else:
        complex_str = None

    return bool_error, text_error, complex_str
