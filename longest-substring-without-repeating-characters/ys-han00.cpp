class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        unordered_map<char, int> mp;

        for(int i = 0; i < s.size(); i++) {
            if(mp[s[i]] == 0) { 
                mp[s[i]] = i;
                ans = max(ans, (int)mp.size());
            }
            else {
                int tmp = mp[s[i]];
                for (auto it = mp.begin(); it != mp.end(); ) {
                    it->second -= tmp;
                    if (it->second < 0)
                        it = mp.erase(it); 
                    else
                        it++;
                }
                mp[s[i]] = i;
            }
        }
        
        return ans;
    }
};

