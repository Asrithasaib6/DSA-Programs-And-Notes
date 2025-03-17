#include<iostream>
#include<string>
using namespace std;
int main()
{
    string str1="Asritha sai";
    string :: iterator it;
    for(it=str1.begin();it!=str1.end();it++)
    {
        cout<<*it;
    }
    str1.append("Morampudi");
    cout<<str1;

    //substring
    cout<<str1.substr(3,2);

    //finding content
    cout<<str1.find("Asri");


}