#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector <int> v(9);
    int sum = 0, answerArr[7];
    int a = 0, b = 0;

    for(int i = 0 ; i < 9 ; i++){
        cin >> v[i];
        sum += v[i];
    }

    for(int i = 0; i < 9 ; i++){
        for(int j = i + 1 ; j < 9 ; j++){
            if(v[i] + v[j] == (sum - 100)){
                v.erase(v.begin() + j);
                v.erase(v.begin() + i);
                break; // 반복문 종료
            }
        }
        if(v.size() == 7) break;
    }

    sort(v.begin(),v.end());

    for(int i = 0 ; i < 7 ; i++){
        cout << v[i] << '\n';
    }
    return 0;
}