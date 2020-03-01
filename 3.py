"""
a,pre,su=0,0,0
for i in range(1,11):
    if i==1:
        su=1+pre
        print(su)
        pre=1
    a=su
    su=su+pre
    pre=a
    print(su)
"""
# n1,n2,item,count=0,1,10,2
# print(n1,",",n2,end=",")
# while count < item:
#     nth=n1+n2
#     print(nth,end=",")
#     n1=n2
#     n2=nth
#     count+=1
d={
    'a':{'name':'xiaoming','age':'11'},
    'b':{'name':'xiaohong','age':'12'},
}
print(d['a']['age'])