#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
vector<int> hashTable[66013];



void Add(int X){

    hashTable[X%66013].push_back(X);
}

void Erase(int X){

    int index = X % 66013;

    for(int i = 0; i < hashTable[index].size(); i++)

            if(hashTable[index][i] == X)
                hashTable[index].erase(hashTable[index].begin() + i);
}

int Search(int X){

    int index = X % 66013;

    for(int i=0; i< hashTable[index].size(); i++)
        if(hashTable[index][i] == X)
            return 1;

    return 0;
}

int main(){

    ifstream f("hashuri.in");
    ofstream g("hashuri.out");

    int n, operation, nr;
    f >> n;
    for (int i=1; i<=n; i++){
        f >> operation >> nr;

        if(operation == 1)
            Add(nr);
        else
            if(operation== 2)
                Erase(nr);
            else
                g << Search(nr) << '\n';
    }

    f.close();
    g.close();
}
