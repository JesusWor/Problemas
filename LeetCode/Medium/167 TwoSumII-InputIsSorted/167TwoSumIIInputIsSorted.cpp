#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size() - 1;
        while (i < j) {
            int sum_target = numbers[i] + numbers[j];
            if (sum_target == target) {
                return {i + 1, j + 1};
            } else if (sum_target < target) {
                i++;
            } else {
                j--;
            }
        }
        return {};
    }
};

int main() {
    Solution sol;
    vector<int> numbers = {2, 7, 11, 15};
    int target = 9;
    vector<int> resultado = sol.twoSum(numbers, target);
    if (!resultado.empty()) {
        cout << "[" << resultado[0] << ", " << resultado[1] << "]" << endl;
    }
    return 0;
}