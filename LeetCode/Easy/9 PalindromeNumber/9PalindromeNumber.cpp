#include <iostream>

class Solution
{
public:
    bool isPalindrome(int x)
    {
        if (x < 0)
        {
            return false;
        }
        long long reversed = 0;
        long long temp = x;
        while (temp != 0)
        {
            int digit = temp % 10;
            reversed = reversed * 10 + digit;
            temp /= 10;
        }
        return (reversed == x);
    }
};

int main()
{
    Solution sol;

    int x1 = 121;
    std::cout << "x = " << x1 << " -> Es palindromo: "
               << (sol.isPalindrome(x1) ? "true" : "false") << std::endl;

    int x2 = -121;
    std::cout << "x = " << x2 << " -> Es palindromo: "
               << (sol.isPalindrome(x2) ? "true" : "false") << std::endl;

    int x3 = 10;
    std::cout << "x = " << x3 << " -> Es palindromo: "
               << (sol.isPalindrome(x3) ? "true" : "false") << std::endl;

    return 0;
}