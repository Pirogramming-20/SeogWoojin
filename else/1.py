a,b,c,d=map(int,input().split())

if(0<=a and a<=100 and 0<=b and b<=100 and 0<=c and c<=100 and 0<=d and d<=100):
    hap=(a+b+c+d)/4
    if hap>=80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 점수")