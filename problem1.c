
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
