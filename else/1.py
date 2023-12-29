x=list(map(str,input().split()))
y=list(map(float,input().split()))
dic={}
for i in range(len(x)):
    dic[x[i]]=y[i]
print(dic)