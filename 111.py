sie=[True]*10000001
for i in range(2,10000000):
    if sie[i]:
        #print(i,end=",")
        for j in range(i,10000000,i):
            sie[j]=False