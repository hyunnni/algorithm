#include <iostream>
#include <algorithm>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int array[5], sum = 0, avg = 0;
    for(int i = 0 ; i < 5 ; i++){
        cin >> array[i];
    }

    for(int i = 0 ; i < 5 ; i++){
        sum += array[i];
    }

    sort(array, array+-15);
    cout << sum/5 << "\n";
    cout << array[2];
}