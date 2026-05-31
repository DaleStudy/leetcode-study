class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<int> d(text1.length(), 0);
        int ans = 0;

        for (auto c : text2) 
        {
            int cur = 0;
            for (int i = 0; i < d.size(); i++)
            {
                if (cur < d[i]) 
                {
                    cur = d[i];
                }
                else if (c == text1[i])
                {
                    d[i] = cur + 1;
                    ans = max(ans, cur + 1);
                }
            }
        }

        return ans;
    }
};
