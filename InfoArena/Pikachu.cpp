
#include <iostream>
#include <fstream>

using namespace std;


int n, k;
long long V[100005];

long long find(long long x)
{
    long long out = 1e18;
    long long aux = 0;
    for (int i = 0; i < n; i++)
    {
        aux += abs(V[i] - x);
        if (i >= k)
            aux -= abs(V[i - k] - x);
        if (i >= k - 1)
            out = min(out, aux);
    }
    return out;
}

int main()
{

    ifstream f("pikachu.in");
    ofstream g("pikachu.out");
    f >> n >> k;

    for (int i = 0; i < n; i++)
        f >> V[i];


    long long left = 0;
    long long right = 2e9;
    while (left <= right)
    {
        long long m = (left + right) >> 1;
        if (find(m - 1) > find(m + 1))
            left = m + 1;
        else
            right = m - 1;
    }


    g << find(left);

    g.close();
    f.close();
    return 0;
}
