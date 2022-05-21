import numpy as nd
ls1=[]
r,c=map(int,input().split())
for i in range(r):
    out=list(map(int,input().split()))
    ls1.append(out)
m=nd.array(ls1)
print(m.T)
print(m.flatten())
