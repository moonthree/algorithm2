#bubble sort

a = [8, 3, 12, 10, 1]

# for i in range(len(a)-1):
#     if a[i] > a[i+1]:
#         a[i], a[i+1] = a[i+1], a[i]
# for i in range(len(a)-2):
#     if a[i] > a[i+1]:
#         a[i], a[i+1] = a[i+1], a[i]
# for i in range(len(a)-3):
#     if a[i] > a[i+1]:
#         a[i], a[i+1] = a[i+1], a[i]
# for i in range(len(a)-4):
#     if a[i] > a[i+1]:
#         a[i], a[i+1] = a[i+1], a[i]
# print(a)

for i in range(len(a)-1, 0, -1):
    for j in range(0, i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1], a[j]
print(a)

# for i in range(len(a)):
#     for j in range(0, len(a)-2-i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]