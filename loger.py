from datetime import datetime

def dif_log(x):
    time = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    with open('surveillance.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{time}:  {x}\n')
        
x = 'ghfjutgjtgot'
print(dif_log(x))