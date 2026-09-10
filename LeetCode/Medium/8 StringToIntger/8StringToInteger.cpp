#include <iostream>
#include <string>
#include <climits>
#include <cctype>

using namespace std;

class Solution {
public:
    int myAtoi(string s) {
        int i = 0, n = s.length(), sign = 1;
        long result = 0; // long para poder comparar sin desbordar antes de saturar

        // salta espacios en blanco iniciales
        while (i < n && s[i] == ' ') {
            i++;
        }

        // detecta signo opcional, una sola vez
        if (i < n && (s[i] == '+' || s[i] == '-')) {
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }

        // acumula digitos consecutivos, se detiene en el primer no-digito
        while (i < n && isdigit(s[i])) {
            int digit = s[i] - '0';
            if (result > INT_MAX / 10 ||
                (result == INT_MAX / 10 && digit > 7)) {
                return (sign == 1) ? INT_MAX : INT_MIN;
            }
            result = result * 10 + digit;
            i++;
        }

        return static_cast<int>(result * sign);
    }
};

int main() {
    Solution sol;

    cout << sol.myAtoi("42") << endl;
    cout << sol.myAtoi("   -042") << endl;
    cout << sol.myAtoi("1337c0d3") << endl;
    cout << sol.myAtoi("0-1") << endl;
    cout << sol.myAtoi("words and 987") << endl;

    return 0;
}