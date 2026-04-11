#include <iostream>
#include <vector>

using namespace std;

int removeDuplicates(vector<int>& nums) {
    if(nums.empty()) return 0;
    int i=0,
        n=nums.size();
    for(int j=1; j<n; j++){
        if(nums[j] != nums[i]){
            i++;
            nums[i]=nums[j];
        }
    }
    return i+1;
}