#include <iostream>
#include <bits/stdc++.h>
using namespace std;


ifstream f("alibaba.in");
ofstream g("alibaba.out");

int main(){

    char nr[10001];
    int n, k, index = 0, aux;

    f >> n >> k;
    aux = k;

    for(int i = 0; i < n; i++){
        f >> nr[index];
        while(index > 0 && nr[index - 1] < nr[index] && aux != 0){
            nr[index - 1] = nr[index];
            aux--; index--;
        }
    index ++;
    }

    for(int i = 0; i < n - k; i++)
        g << nr[i];

    f.close();
    g.close();
    return 0;
}
