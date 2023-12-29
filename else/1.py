a,b=map(int,input().split())

for i in range(a,b+1):
    print('Fizz'*(i%5==0) + 'Buzz'*(i%7==0) or i)