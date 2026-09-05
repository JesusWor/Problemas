#include <iostream>
#include <String>
#include <algorithm>
using namespace std;

bool isPalindrome(string s)
{
    string filtered;
    // Permitira filtrar los caracteres alfabeticos y los convertira en minuscilas ademas de que se almacenaran en una variable
    for (char c : s)
    {
        if (isalnum(c))
        {
            filtered += tolower(c);
        }
    }
    string reversed = filtered;
    reverse(reversed.begin(), reversed.end());
    return filtered == reversed;
}

int main()
{
    string palabra;
    cout << "Ingrese una palabra: ";
    cin >> palabra;

    cout << isPalindrome(palabra);
    return 0;
}