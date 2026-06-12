#include <bits/stdc++.h>

using namespace std;

int f(int x){
    if(x <= 0) return 0;
    if(x < 10) return x;
    int count = 9;

    int limit = x / 11;
    count += min(9, limit);
    return count;
}

int main() {
    int Q, L, R;
    cin >> Q;
    for (int i=0; i<Q; i++){
        cin >> L >> R;
        int salida = f(R) - f(L-1);
        cout << salida << endl;
    }
}