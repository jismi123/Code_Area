x=int(input())
arr=list(map(int,input().split()))
n=len(arr)
count=0
for i in range(n):
    if arr[i]==1:
        count=count+1
print(count)

