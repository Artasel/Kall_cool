from datetime import datetime

def dif_log(str):
    with open('surveillance.txt', 'a+', encoding='UTF-8') as file:
        file.write(f'{datetime.now()}:  {str}\n')
        
