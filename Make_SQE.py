
"""
최초 100회에서 일정 수치 이상 확률 시 검증 절차
10000회 에서 4900회 넘기면 2차 검증 통과
그 이후 10만회를 더 돌려 11만회 평균 수치 확인

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
    cnta=0
    cntb=0
    cntc=0
    for i in range(0, 10000):
        random.shuffle(a)
        random.shuffle(b)
        random.shuffle(c)
        k = 0
        if a[0] > b[0]:
            cnta = cnta + 1
        if b[0] > c[0]:
            cntb = cntb + 1
        if c[0] > a[0]:
            cntc = cntc + 1

    if cnta>4950 and cntb>4950 and cntc>4950:
        tota+=cnta
        totb+=cntb
        totc+=cntc
        print("최초 1만회 검증 : %d %d %d" % (cnta,cntb,cntc))
        for k in range(0,10):
            cnta=0
            cntb=0
            cntc=0
            for i in range(0, 10000):
                random.shuffle(a)
                random.shuffle(b)
                random.shuffle(c)
                k = 0
                if a[0] > b[0]:
                    cnta = cnta + 1
                if b[0] > c[0]:
                    cntb = cntb + 1
                if c[0] > a[0]:
                    cntc = cntc + 1
            tota+=cnta
            totb+=cntb
            totc+=cntc
        print("11만회 시행 평균 : %d %d %d"%(tota/11,totb/11,totc/11))
        return True
    else:
        return False

for i in range(0,300000):
    count=count+1
    a = make(sum)
    b = make(sum)
    c = make(sum)
    n = 100
    counta = 0
    countb = 0
    countc = 0
    for i in range(0, n):
        random.shuffle(a)
        random.shuffle(b)
        if a[0] > b[0]:
            counta = counta + 1
    for i in range(0, n):
        random.shuffle(b)
        random.shuffle(c)
        if b[0] > c[0]:
            countb = countb + 1
    for i in range(0, n):
        random.shuffle(c)
        random.shuffle(a)
        if c[0] > a[0]:
            countc = countc + 1
    if counta > n/2.2 and countb >n/2.2 and countc > n/2.2:
        #print("%d %d %d" % (counta, countb, countc))
        if chk(a,b,c):
            print(a)
            print(b)
            print(c)
            print()
print("Search finished")
input()