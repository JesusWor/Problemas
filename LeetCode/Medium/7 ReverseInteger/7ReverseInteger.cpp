#include <iostream>
#include <climits>  // para INT_MAX e INT_MIN

using namespace std;

class Solution {
public:
    int reverse(int x) {
        int reversed = 0;
        while (x != 0) {
            int digit = x % 10;
            if (reversed > INT_MAX / 10 || reversed < INT_MIN / 10) {
                return 0;
            }
            reversed = reversed * 10 + digit;
            x /= 10;
        }
        return reversed;
    }
};

int main() {
    Solution sol;
    cout << sol.reverse(123) << endl;
    cout << sol.reverse(456) << endl;
    cout << sol.reverse(-123) << endl;
    cout << sol.reverse(1534236469) << endl;

    return 0;
}