#include <bits/stdc++.h>

using namespace std;

int main() {
    int A, 
        B, 
        C, 
        contador = 0, 
        comprados = 1, 
        acumulado = 0;
    cin >> A >> B >> C;
    while (comprados < C) {
        acumulado += B;
        if (acumulado >= A) {
            B += B;
            comprados++;
        }
        contador++;
    }
    cout<<contador;
    return 0;
}