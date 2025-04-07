class Solution {
    public:
        int longestConsecutive(vector<int>& nums) {
            int cnt = 1;
            int max = 0;
    
            if(nums.size() == 0)
                return 0;
    
            sort(nums.begin(), nums.end());
    
            for(int i = 1; i < nums.size(); i++){
                if(nums[i] == nums[i-1] + 1)
                    cnt++;
                else if(nums[i] == nums[i-1])
                    continue;
                else{
                    if(max < cnt)
                        max = cnt;
    
                    cnt = 1;
                }
            }
    
            if(max < cnt)
                return cnt;
    
            return max;
        }
    };
