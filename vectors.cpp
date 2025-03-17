#include<iostream>
#include<vector>
using namespace std;
int main()
{
    //example of vectors
    vector<int> num;
    num.push_back(1);
    num.push_back(2);
    num.push_back(3);
    for(int i=0;i<3;i++)
    {
        cout<<num[i];
    }
    cout << "Size :" << num.size()<<endl;
    //overloading
    vector<int> num1(10,5);//here printing 5 ten times
    for(int i=0;i<num1.size();i++)
    {
        cout<<num1[i]<<endl;
    }
    //how to access and modify elements in vector
    vector<int> v={1,2,3,4};
    cout<<v[0]<<endl;
    cout<v.at[0];
}