class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        this->s = s;
        return solve(0, wordDict);
    }

    // substr 시작 인덱스와 wordDict를 입력으로 받음
    bool solve(int start, vector<string>& wordDict)
    {
        // 이미 계산한 적 있으면 메모이제이션으로 해결
        if (memo.contains(start))
        {
            return memo[start];
        }

        // 베이스컨디션 -> 끝까지 도달했으면 true
        if (start == s.size())
        {
            return true;
        }

        for (auto& str : wordDict)
        {
            // wordDict에 있는 단어들로 시작하는지 확인
            if (s.substr(start, str.size()) == str)
            {
                // 그리고 그 뒷 부분도 재귀를 통해 확인
                if (solve(start + str.size(), wordDict))
                {
                    // 뒷 부분까지 통과했으면 true
                    memo[start] = true;
                    return true;
                }
            }
        }

        // 통과 못했으면 false
        memo[start] = false;
        return false;
    }

private:
    string s;
    unordered_map<int, bool> memo; // 메모이제이션
};
