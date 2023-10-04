arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr3=list(map(int,input().split()))
for i in arr1:
    if i in arr2 and arr3:
        print(i,end=" ")
