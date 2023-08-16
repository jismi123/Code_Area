#include<stdio.h>
int differenceofSum(int n,int m)
{
    int sum=0,sum1=0;
    
    for(int i=1;i<=m;i++)
    {
        if(i%n==0) 
            sum=sum+i;  
        else 
            sum1=sum1+i;
    }
    if (sum1 > sum)
        return sum1 - sum;
    else
        return sum - sum1;
}
int main()
{
    int n,m;
    scanf("%d",&n);
    scanf("%d",&m);
    printf("%d",differenceofSum(n,m));
}
