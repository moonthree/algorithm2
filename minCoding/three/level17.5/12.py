arr = [[chr(65 + i + 5*j) for i in range(5)] for j in range(5)]

spell = input()

spell_y = 0
spell_x = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if spell == arr[i][j]:
            spell_y = i
            spell_x = j

print(f'{spell_y-2},{spell_x-2}')