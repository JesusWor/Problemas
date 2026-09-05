#include <iostream>
#include <stack>
#include <unordered_map>

class Solution
{
public:
    bool isValid(std::string s)
    {
        std::stack<char> stack;
        std::unordered_map<char, char> matchingBrackets = {
            {')', '('},
            {'}', '{'},
            {']', '['}};

        for (char c : s)
        {
            if (c == '(' || c == '{' || c == '[')
            {
                stack.push(c);
            }
            else
            {
                if (stack.empty() || stack.top() != matchingBrackets[c])
                {
                    return false;
                }
                stack.pop();
            }
        }

        return stack.empty();
    }
};
