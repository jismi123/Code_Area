#include<stdio.h>
int main()

{
    int n,i,j,a[100],temp,b,res,sum;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(a[j]>a[j+1])
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    }
    
b=n/2;
if(n%2==0)
{
    sum=a[b]+a[b-1];
    res=sum/2;
    printf("%d",res);
}
else
{
    printf("%d",a[b]);
}
        
    
}
