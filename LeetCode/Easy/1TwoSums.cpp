class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> mapa;
        for (int i = 0; i < nums.size(); i++)
        {
            int comple = target - nums[i];
            if (mapa.find(comple) != mapa.end())
            {
                return {mapa[comple], i};
            }
            mapa[nums[i]] = i;
        }
        return {};
    }
};