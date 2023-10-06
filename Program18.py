def close(arr,x):
    left=0
    right=len(arr)-1
    closest_sum=float('inf')
    pair=None
    while(left<right):
        current_sum=arr[left]+arr[right]
        if abs(current_sum-x)<abs(closest_sum-x):
            closest_sum=current_sum
            pair=(arr[left],arr[right])
        if current_sum<x:
            left=left+1 
        else:
            right=right-1 
    print(pair)
            
    
n,x=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
close(arr,x)
