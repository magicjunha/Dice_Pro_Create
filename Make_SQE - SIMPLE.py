
"""
최초 100회에서 일정 수치 이상 확률 시 검증 절차
10000회 에서 4900회 넘기면 2차 검증 통과
그 이후 실확률 계산 및 출력

각 숫자 범위 : 0~6
합 : 18
"""
import random

#sum = int(input("합을 입력하세요 : "))
sum = 18
def go(sum, list):
    chk=0
    for i in range(0,6):
        chk=chk+list[i]
    if chk==sum:
        return False
    else:
        return True

def make(sum):
    temp=[0,0,0,0,0,0]
    while(go(sum,temp)):
        for i in range(0,6):
            temp[i]=random.randrange(0,7)
    return temp
count=0

def chk(a,b,c):
    tota=0
    totb=0
    totc=0
    for i in range(0,6):
        for j in range(0,6):
            if a[i]>b[j]: tota+=1
            if b[i]>c[j]: totb+=1
            if c[i]>a[j]: totc+=1
    if tota>18 and totb>18 and totc>18:
        print("확률 : %.3f %.3f %.3f"%(tota/36,totb/36,totc/36))
        return True
    else : return False

for i in range(0,100000):
    count=count+1
    a = make(sum)
    b = make(sum)
    c = make(sum)
    if chk(a,b,c):
        print(a)
        print(b)
        print(c)
        print()
print("Search finished")
input()