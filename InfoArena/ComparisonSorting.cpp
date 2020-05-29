#include <iostream>
#include <fstream>
using namespace std;
ifstream f ("algsort.in");
ofstream g ("algsort.out");
int V[500005];

void merge(int L, int M, int R)
{
    int n1, n2, i, j, k;

    n1=M-L+1;
    n2=R-M;

    int a[n1], b[n2];

    for(i=1; i<=n1; i++){
        a[i]=V[L-1+i];
    }

    for(j=1; j<=n2; j++){
        b[j]=V[M+j];
    }

    i=1; j=1; k=L;

    while(i<=n1 && j<=n2){
        if(a[i]<=b[j]){
            V[k]=a[i];
            i++;
        }
        else{
            V[k]=b[j];
            j++;
        }
        k++;
    }

    while(i<=n1){
        V[k]=a[i];
        i++;
        k++;
    }

    while(j<=n2){
        V[k]=b[j];
        j++;
        k++;
    }
}
void mergeSort(int L, int R)
{
    int M;
    if(L<R){
        M=(L+R)/2;
        mergeSort(L,M);
        mergeSort(M+1,R);
        merge(L,M,R);
    }
}

int main()
{
    int n, i;
    f>>n;
    for(i=1; i<=n; i++)
        f>>V[i];
    mergeSort(1, n);
    for(i=1; i<=n; i++)
        g<<V[i]<<" ";
    return 0;
}
