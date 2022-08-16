spell = input()
ord_spell = ord(spell)

for i in range(-3, 4):
    if ord_spell+i < 65:
        print(chr(90-65+ord_spell+i+1), end='')
    elif ord_spell+i > 90:
        print(chr(65+90-ord_spell+i-3), end='')
    else:
        print(chr(ord_spell+i), end='')