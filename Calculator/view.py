import logger as lgc

def view(data):
    lgc.logg(data)
    print(data)


def get():
    x = input('enter: ')
    return x
