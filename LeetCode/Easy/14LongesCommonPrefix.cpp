#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string longestCommonPrefix(vector<string> &strs)
{
    if (strs.empty())
        return ""; // Edge case: empty input

    string prefix = strs[0]; // Start with the first string as the prefix

    for (int i = 1; i < strs.size(); i++)
    {
        // Compare the current prefix with the next string
        while (strs[i].find(prefix) != 0)
        {                                                   // Check if prefix is not a prefix of strs[i]
            prefix = prefix.substr(0, prefix.length() - 1); // Reduce the prefix by one character
            if (prefix.empty())
                return ""; // If prefix becomes empty, return
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
                if (ch == s[i])
                {
                    continue;
                }
                else
                {
                    return prefix;
                }
            }
            prefix += ch;
        }
        return prefix;
    }
};