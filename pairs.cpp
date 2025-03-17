#include<iostream>
#include<vector>
#include<utility>
using namespace std;
int main()
{
    pair<int,float> p(23,45.56);
    cout<<p.first<<" "<<p.second<<endl;
    pair<int,int> p1(23,34);
    cout<<p1.first<<" "<<p1.second<<endl;

    //vectors of pairs
    vector<pair<int,float>> sd={{1,23.5},{2,56.7}};
    for(int i=0;i<sd.size();i++)
    {
        cout<< sd[i].first<<endl;
    }
    return 0;


}