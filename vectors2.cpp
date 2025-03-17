#include<iostream>
#include<vector>
using namespace std;
int main()
{
    //Iteratros and reverse iterator in cpp
    vector<int> v={1,2,3,4,5,6,7};
    vector<int>:: iterator it;
    cout<<*(v.begin())<<endl;
    cout<<*(v.end()-1)<<endl;
    for(it=v.begin();it!=v.end();it++)
    {
        cout<<*it<<endl;
    }
    //reverse iterator
    vector<int>:: reverse_iterator rit;
    for(rit=v.rbegin();rit!=v.rend();rit++)
    {
        cout<<*rit<<endl;
    }

}