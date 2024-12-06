class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        const int INF = 987654321;
        int temp = INF, ret = 0, cur = 0;

        sort(nums.begin(), nums.end());
        for(int a : nums){
            if(a == temp)continue;
            if(temp == INF || temp + 1 == a){
                cur++; temp = a;
            } else {
                ret = max(ret, cur); 
                cur = 1;
                temp = a;
            }
        }
        ret = max(ret, cur);
        return ret;
    }
};