n=int(input())
k=1
for i in range(n):
    blank=' '*(n-i-1)
    print(blank, end='')
    print('*'*k)
    k=k+2
