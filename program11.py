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
    print(msf)
arr=list(map(int,input().split()))
maxarray(arr,len(arr))
