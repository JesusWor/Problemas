#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int ans = 0;
        while (l < r) {
            int ancho = r - l;
            int alto = min(height[r], height[l]);
            int area = ancho * alto;
            ans = max(ans, area);
            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    int resultado = sol.maxArea(height);
    cout << resultado << endl;
    return 0;
}