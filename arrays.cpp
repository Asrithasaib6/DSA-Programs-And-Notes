#include<iostream>
using namespace std;
int main()
{
    int arr[15]={0};
    arr[0]=10;
    arr[14]=150;
    cout<<"the elements in the array are:"<<endl;
    for(int i=0;i<15;i++)
    {
        cout<<arr[i]<<endl;
    }
    return 0;

}