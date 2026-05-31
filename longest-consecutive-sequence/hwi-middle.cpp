class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty())
        {
            return 0;
        }
        
        unordered_set<int> s;
        s.reserve(nums.size());
        s.max_load_factor(0.4f);
        s.insert(nums.begin(), nums.end());

        int ans = 0;
        for(auto& e : s)
        {
            if (s.contains(e - 1))
            {
                continue;
            }

            int con = 1;
            int num = e;
            while (true)
            {
                num++;
                if(!s.contains(num))
                {
                    break;
                }

                con++;
            }
            ans = max(ans, con);
        }

        return ans;
    }
};
