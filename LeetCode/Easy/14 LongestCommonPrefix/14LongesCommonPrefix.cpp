#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// Solcion de chatgpt
string longestCommonPrefix(vector<string> &strs)
{
    if (strs.empty())
        return "";

    string prefix = strs[0];

    for (int i = 1; i < strs.size(); i++)
    {
        while (strs[i].find(prefix) != 0)
        {
            prefix = prefix.substr(0, prefix.length() - 1); // Reduce el prefijo caracter por caracter
            if (prefix.empty())
                return "";
        }
    }

    return prefix;
}

class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        if (strs.size() == 0)
            return "";

        string prefix = "";
        for (int i = 0; i < strs[0].length(); i++)
        {
            char ch = strs[0][i];
            for (string s : strs)
            {
                // Validación agregada: evita acceso fuera de rango si "s"
                // es mas corto que strs[0] (en el codigo original esto
                // era undefined behavior si i >= s.length()).
                if (i >= s.length() || ch != s[i])
                {
                    return prefix;
                }
            }
            prefix += ch;
        }
        return prefix;
    }
};

int main()
{
    Solution sol;
    vector<string> ejemplo1 = {"flower", "flow", "flight"};
    cout << "Prefijo comun: \"" << sol.longestCommonPrefix(ejemplo1) << "\"" << endl;

    return 0;
}