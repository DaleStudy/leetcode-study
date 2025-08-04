class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> isNum;
        int ans = 0;
        for (auto num : nums)
            isNum.insert(num);
        for (auto num : isNum) // (auto num : nums)하면 틀린다 일부러 시작하는 위치를 많이 넣는 테스트케이스 존재
        {
            if (isNum.find(num - 1) == isNum.end() && isNum.find(num) !=isNum.end())
            {
                int curLen = 0;
                for (int seqNum = num; isNum.find(seqNum) != isNum.end(); seqNum++)
                {
                    curLen += 1;
                }
                ans = max(ans, curLen);
            }
        }
        return ans;
    }
};
