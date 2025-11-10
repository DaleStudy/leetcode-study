class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        auto s = unordered_set<int>();
        for(int it : nums) {
            s.insert(it);
        }

        int m = 0;
        for(int it : s) {
            if(s.count(it-1) > 0) continue;
            
            int cnt = 0;
            while(s.count(it+cnt) > 0){
                cnt++;
            }
            m = max(m, cnt);
        }

        return m;
    }
};
