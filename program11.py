from sys import maxsize
def maxarray(arr,size):
    mef=0
    msf=-maxsize-1
    for i in range(0,size):
        mef=mef+arr[i]
        if mef>msf:
            msf=mef
        if mef<0:
            mef=0
    print(msf) #printing just sum
arr=list(map(int,input().split()))
maxarray(arr,len(arr))
"""
printing sum and the subarray
from sys import maxsize
def maxarray(arr,size):
    mef=0
    msf=-maxsize-1
    start=0
    end=0
    s=0
    for i in range(0,size):
        mef=mef+arr[i]
        if msf<mef:
            msf=mef
            start=s 
            end=i
        if mef<0:
            mef=0
            s=i+1
    print(msf)
    for i in range(start,end+1):
        print(arr[i],end=" ")
    
arr=list(map(int,input().split()))
maxarray(arr,len(arr))

"""
