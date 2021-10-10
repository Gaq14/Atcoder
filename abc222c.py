n,m=map(int,input().split())
a=[input() for i in range(2*n)]
s=[0]*2*n
l=list(range(2*n))
r=l

for i in range(m):
  for k in range(n):
    t1=a[r[2*k]][i]
    t2=a[r[2*k+1]][i]
    if t1+t2=='GC' or t1+t2=='CP' or t1+t2=='PG':
      s[r[2*k]]-=1
    elif t1!=t2:
      s[r[2*k+1]]-=1
  r=sorted(l, key=lambda i:s[i])
for p in r:
  print(p+1)