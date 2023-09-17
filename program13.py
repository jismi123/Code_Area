arr=list(map(int,input().split()))
n=len(arr)
for i in range(n):
    for j in range(i,n+1):
        for k in range(i,j):
            print(arr[k],end=" ")
        print()
            
    
