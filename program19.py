def closest(arr1,arr2,x):
    closest_sum=float('inf')
    pair=None
    for num1 in arr1:
        target=num1-x
        left=0
        right=len(arr2)-1
        while(left<right):
            mid=left+(right-left)//2 
            num2=arr2[mid]
            current_sum=num1+num2
            if abs(current_sum-x)<abs(closest_sum-x):
                closest_sum=current_sum 
                pair=(num1,num2)
            if current_sum<x:
                left=mid+1 
            else:
                right=mid-1
    print(pair)            
x=int(input())
n=int(input())
arr1=list(map(int,input().split()))
n2=int(input())
arr2=list(map(int,input().split()))
arr1.sort()
arr2.sort()
closest(arr1,arr2,x)
