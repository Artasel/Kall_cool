
'''
Модуль для действий с вещественными числами

'''
def sum_num(a, b):    
    ''' 
    Функция сложения двух чисел
    '''
    return a + b


def sub_num(a, b):    
    ''' 
    Функция вычитания двух чисел
    '''
    return a - b

def div_num(a, b):    
    ''' 
    Функция деления двух чисел
    '''
    if b == 0:
        return 'Деление на 0'
    else: 
        return a / b

def mult_num(a, b):    
    ''' 
    Функция умножения двух чисел
    '''
    return a * b
