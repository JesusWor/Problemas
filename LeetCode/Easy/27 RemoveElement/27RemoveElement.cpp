#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {0, 1, 2, 2, 3, 0, 4, 2};
    int val = 2;

    int k = sol.removeElement(nums, val);

    cout << "k: " << k << endl;
    cout << "Vector modificado: [";
    for (int i = 0; i < k; ++i) {
        cout << nums[i] << (i == k - 1 ? "" : ", ");
    }
    cout << "]" << endl;

    return 0;
}