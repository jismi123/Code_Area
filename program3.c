#include<stdio.h>
#include<string.h>
int CheckPassword(char str[],int n)
{
    int numcount=0,chcount=0;
    if(n<4)
        return 0;
    if((str[0]-'0')>=0 && (str[0]-'0')<=9)
        return 0;
    for(int i=0;i<n;i++)
    {
       if(str[i]==' ' || str[i]=='/')
            return 0;
       if((str[i]-'0')>=0 && (str[i]-'0')<=9)
            numcount++;
       if(str[i]>='A' && str[i]<='Z')
            chcount++;
    }
    if(numcount>0 && chcount>0)
        return 1;
}
int main()
{
    char str[100];
    fgets(str,sizeof(str),stdin);
    int n=strlen(str);
    if(str[n-1]=='\n')
    {
        str[n-1]='\0';
        n--;
    }
    printf("%d",CheckPassword(str,n));
}
