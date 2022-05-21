import numpy as np
r,c=map(int,input().split())
ls1=[]
ls2=[]
for i in range(r):
    ele=list(map(int,input().split()))
    ls1.append(ele)
for i in range(c):
    ele=list(map(int,input().split()))
    ls2.append(ele)
m1=np.array(ls1)
m2=np.array(ls2)


print('add=',np.add(m1,m2))
print('sub='np.subtract(m1,m2))
print('mul='np.multiply(m1,m2))
print('divide=',np.floor_divide(m1,m2))
print(np.mod(m1,m2))
print(np.power(m1,m2))
