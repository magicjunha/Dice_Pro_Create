a=input().split(' ')
b=input().split(' ')
c=input().split(' ')
d=0
for i in range(0,6):
    for j in range(0,6):
        for k in range(0,6):
            if a[i]>b[j] and a[i]>c[k]:
                d+=1/216
print(d)
d=0

a=b=c=a
for i in range(0,6):
    for j in range(0,6):
        for k in range(0,6):
            if a[i]>b[j] and a[i]>c[k]:
                d+=1/216
print(d)

d=0
a=b=c=a
for i in range(0,6):
    for j in range(0,6):
        for k in range(0,6):
            if a[i]>b[j] and a[i]>c[k]:
                d+=1/216
print(d)

