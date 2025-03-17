#include<stdio.h>
int main()
{
    /*int a=5;
    int b=5;
    int *p=&a;
    printf("%d",p);
    return 0;*/
    int a[5]={1,2,3,4,5};
    int b[5]={1,2,3,4,5};
    int *p=&a[0];
    int *q=&b[3];
    int d=q-p;
    printf("%d",d);
    return 0;

}