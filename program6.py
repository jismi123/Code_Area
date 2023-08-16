def LargeSmallSum(arr):
    length = len(arr)
    
    if length == 0 or length <= 3:
        return 0
    
    even = []
    odd = []
    
    for i in range(length):
        if i % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    
    even.sort()
    odd.sort()
    
    second_largest_even = even[-2]
    second_smallest_odd = odd[1]
    
    return second_largest_even + second_smallest_odd


arr = list(map(int, input().split()))
result = LargeSmallSum(arr)
print(result)
