class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v(2);
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i)
        {
            int num = nums[i];
            if (m.contains(target - num))
            {
                v[0] = m[target - num];
                v[1] = i;
                return v;
            }

            m[num] = i;
        }

        v[0] = -1;
        v[1] = -1;
        return v;
    }
};
