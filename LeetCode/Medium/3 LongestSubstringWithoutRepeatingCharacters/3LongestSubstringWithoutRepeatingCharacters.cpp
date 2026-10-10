#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_map<char, int> last;
        int maximum = 0;
        int start = 0;

        for(int i=0; i < s.size(); i++){
            char c = s[i];
            if(last.count(c) && last[c] >= start){
                start = last[c] + 1;
            }
            last[c] = i;
            maximum = std::max(maximum, i-start+1);
        }
        return maximum;
    }
};

int main() {
    Solution sol;
    string s = "abcabcbb";
    int resultado = sol.lengthOfLongestSubstring(s);
    cout << resultado << endl;
    return 0;
}