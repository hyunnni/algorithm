#include <iostream>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, result = 1;
    cin>>n;
    for(int i = 1; i < n+1; i++){
        result *= i;
    }
    cout<<result;
}