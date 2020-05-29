#include <fstream>
#include <iostream>
using namespace std;


int zeroCounter(int x){

    int out=0, p=5;

    while(x/p>0){
        out+=x/p;
        p*=5;
    }
    return out;
}

int main()
{
    ifstream f("fact.in");
    ofstream g("fact.out");

    int k,left,right;

    f >> k;

    if(k==0){ g << 1; }

    left=5;
    right=5*k;

    while(left < right){

        int mid = (left + right) / 2;
        if(zeroCounter(mid) < k)
            left = mid + 1;
        else
            right = mid;}

    if(zeroCounter(left) == k)
        g << left;
    else
        g << -1;

    f.close();
    g.close();
}
