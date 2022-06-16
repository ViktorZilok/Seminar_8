from datetime import datetime as dt

def logg(data):
    time = dt.now().strftime('%H:%M')
    with open('logs.txt', 'a', encoding='utf-8') as file:
        file.write('{}; Пример; {}\n'
                   .format(time, data))


