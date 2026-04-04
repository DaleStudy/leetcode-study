class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        this->s = s;
        return solve(0, wordDict);
    }

    bool solve(int start, vector<string>& wordDict)
    {
        if (memo.contains(start))
        {
            return memo[start];
        }

        if (start == s.size())
        {
            return true;
        }

        for (auto& str : wordDict)
        {
            if (s.substr(start, str.size()) == str)
            {
                if (solve(start + str.size(), wordDict))
                {
                    memo[start] = true;
                    return true;
                }
            }
        }

        memo[start] = false;
        return false;
    }

private:
    string s;
    unordered_map<int, bool> memo;
};
