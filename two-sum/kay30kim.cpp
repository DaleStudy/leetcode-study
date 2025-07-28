// 1) Brute Force - two nested for loop
// T(C) : O(N^2)
// 2) sort & two pointer
// T(C) : O(NlogN)
// 3) hash
// T(C) : O(N)


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> indicesVector;
        unordered_map<int, int> numToIdx;
        for (int i = 0; i < nums.size(); i++)
        {
            if(numToIdx.find(target - nums[i]) != numToIdx.end())
            {
                indicesVector.push_back(numToIdx[target - nums[i]]);
                indicesVector.push_back(i);
                break;
            }
            numToIdx[nums[i]] = i;
        }
        return indicesVector;
    }
};
