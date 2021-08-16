import operator
res={}
res['ashutosh']=90
res['ashu']=89
res['as']=90
res['roshan']=97

a = [0] * (len(res))
j = 0
for i in res:
        a[j] = [i, res[i]]
        j += 1
a = sorted(a, key=lambda x: x[0])
a = sorted(a, key=lambda x: x[1],
               reverse=True)


for i in range(len(a)):
    for j in range(2):
        print(a[i][j])
