#include <iostream>
#include <String>
#include <algorithm>


class Solution {
public:
    bool isPalindrome(std::string s)
    {
        std::string filtered;
        // Permitira filtrar los caracteres alfabeticos y los convertira en minuscilas ademas de que se almacenaran en una variable
        for (char c : s)
        {
            if (isalnum(c))
            {
                filtered += tolower(c);
            }
        }
        std::string reversed = filtered;
        reverse(reversed.begin(), reversed.end());
        return filtered == reversed;
    }
};

int main()
{
    Solution sol;
    // Salida esperada ejemplo 1: true
    std::string s = "A man, a plan, a canal: Panama";
    std::cout<<"Salida ejemplo 1: "<<sol.isPalindrome(s)<<std::endl;

    // Salida esperada ejemplo 2: true
    s = " ";
    std::cout<<"Salida ejemplo 2: "<<sol.isPalindrome(s)<<std::endl;
    return 0;
}