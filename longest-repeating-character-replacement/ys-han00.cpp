class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0, right = 0, ans = 0;
        int maxi_cnt = 0;
        map<char, int> cnt;

        while(left < s.size() && right < s.size()) {
            cnt[s[right]]++;
            maxi_cnt = max(maxi_cnt, cnt[s[right]]);
            right++;

            if(right - left - maxi_cnt <= k)
                ans = max(ans, right - left);
            else
                cnt[s[left++]]--;
        }

        return ans;
    }
};

