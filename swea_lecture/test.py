a = int(input())
b = input()

def chicken(num):
    return num + 10

def coke(str):
    return str

def kfc(num, str):
    c = chicken(num)
    d = coke(str)
    print(f'{c}{d}')

def main(a, b):
    kfc(a, b)

main(a, b)