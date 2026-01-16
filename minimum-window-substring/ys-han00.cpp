class Solution {
public:
    string minWindow(string s, string t) {
        int l = 0, substr = 0, min_l = 0, min_r = s.size();
        map<char, int> cnt;
        for(char c : t)
            cnt[c]++;

        for(int r = 0; r < s.size(); r++) {
            if(cnt.find(s[r]) != cnt.end()) {
                if(cnt[s[r]] > 0)
                    substr++;
                cnt[s[r]]--;
            }

            while(substr == t.size()) {
                if(r - l < min_r - min_l) {
                    min_l = l;
                    min_r = r;
                }

                if(cnt.find(s[l]) != cnt.end()) {
                    cnt[s[l]]++;
                    if(cnt[s[l]] > 0)
                        substr--;
                }

                l++;                   
            }
        }        

        string ans = (min_r < s.size() ? s.substr(min_l, min_r - min_l + 1) : "");
        return ans;
    }
};
 
