#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) {
            return s;
        }

        int separation = numRows - 2;
        int n = s.length();

        string resultado = "";

        for (int i = 0; i < numRows; i++) {
            for (int j = i; j < n; ) {
                resultado += s[j];
                if (i == 0 || i == numRows - 1) {
                    j += (2 * separation + 2);
                } else {
                    j += (2 * separation + 2);
                    if (j - (2 * i) < n) {
                        resultado += s[j - (2 * i)];
                    }
                }
            }
        }

        return resultado;
    }
};

int main() {
    Solution sol;
    string s = "PAYPALISHIRING";
    int numRows = 3;

    cout << sol.convert(s, numRows) << endl;

    return 0;
}