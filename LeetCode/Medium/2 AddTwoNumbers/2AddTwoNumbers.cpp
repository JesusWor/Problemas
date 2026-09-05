#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int suma = nums[i] + nums[j];
                if (suma == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> resultado = sol.twoSum(nums, target);
    if (!resultado.empty()) {
        cout << "[" << resultado[0] << ", " << resultado[1] << "]" << endl;
    }
    return 0;
}