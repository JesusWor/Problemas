#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        for (size_t i = 1; i < nums.size(); ++i) {
            nums[i] += nums[i - 1];
        }
        return nums;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 4};
    vector<int> resultado = sol.runningSum(nums);

    cout << "[";
    for (size_t i = 0; i < resultado.size(); ++i) {
        cout << resultado[i] << (i == resultado.size() - 1 ? "" : ", ");
    }
    cout << "]" << endl;

    return 0;
}