from math import ceil
a=[]
for i in range(5):
    a.append(int(input()))

k=ceil(a[1]/a[3])
m=ceil(a[2]/a[4])
if k>m:
    print(a[0]-k)
else:
    print(a[0]-m)