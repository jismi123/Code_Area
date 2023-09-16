str=input()
r=input()
a=len(str)
count=0
for i in range(a):
    if str[i]==r:
        count=count+1 
print(count)
