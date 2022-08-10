from dataclasses import dataclass

@dataclass
class Data:
    a:int = None
    b:int = None

a = Data()
b = Data()

a.x, a.y, a.z = map(int, input().split())
b.x, b.y, b.z = map(int, input().split())

print(a.x + b.x)
print(a.y + b.y)
print(a.z + b.z)