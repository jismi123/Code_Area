/*
Problem Description :
The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i

Note:

    Return -1 if the array is null
    Return 0 if the total amount of food from all houses is not sufficient for all the rats.
    Computed values lie within the integer range.
*/
#include<stdio.h>
int calculate(int,int,int [],int);
int main()
{
    int r,n,i;
    scanf("%d",&r);
    int unit;
    scanf("%d",&unit);
    scanf("%d",&n);
    int arr[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    printf("%d",calculate(r,unit,arr,n));
}
int calculate(int r,int unit,int arr[],int n)
{
    if(n==0)
        return -1;
    int req=r*unit;
    int sum=0,i;
    for(i=0;i<n;i++)
    {
      sum=sum+arr[i];
      if(sum>=req)
      {
          break;
      }
    }
    if(sum<req)
    {
        return 0;
    }
    return (i+1);
}
