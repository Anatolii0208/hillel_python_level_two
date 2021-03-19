a = int(input())
s=['1','2','3','4','5','6','7','8','9','0']
d={}
f=''
e=''
for i in range(a):
  g = input()
  for j in range(len(g)):
    if g[j] not in s:
      f+=g[j]
    else:
      e+=g[j]
  if f in list(d.keys()):
    d[f]+=int(e)
  else:
    d[f]=int(e)
  f=''
  e=''
q = list(d.keys())
q.sort()
for i in q:
  print(f"{i}:{d[i]}")
