
def user_mode(rez: str) -> bool:
    return rez == '1' or rez == '2' or rez == '3'

'''проверка пользователя на ввод в меню'''

def empty_line(rez: str) -> bool:
    s = len(rez)
    return s == 0

'''проверка ввода пустой строки'''

def is_compl(num):
    num1, num2 = num.split(' ')
    return num1.isdigit(), num2.isdigit()
    
'''проверка и разбитие строки на 2 значения'''

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

'''проверяет число на float'''











