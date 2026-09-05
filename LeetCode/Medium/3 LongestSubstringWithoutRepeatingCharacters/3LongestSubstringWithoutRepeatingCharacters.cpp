#include <iostream>
#include <string>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> st;
        int maxLen = 0;
        int i = 0;
        int j = 0;
        int n = s.length();

        while (j < n) {
            if (st.find(s[j]) == st.end()) {
                st.insert(s[j]);
                j++;
                maxLen = max(maxLen, (int)st.size());
            } else {
                st.erase(s[i]);
                i++;
            }
        }
        return maxLen;
    }
};

int main() {
    Solution sol;
    string s = "abcabcbb";
    int resultado = sol.lengthOfLongestSubstring(s);
    cout << resultado << endl;
    return 0;
}