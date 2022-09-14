import random
def r(n):
  global c,v
  c+=1
  v[n]=1,print(n)
  if c==7:return
  while 1:
      p=random.randrange(1,46)
      if v[p]!=1:break
  r(p)
c,v=0,[0]*47
r(random.randrange(1,46))
