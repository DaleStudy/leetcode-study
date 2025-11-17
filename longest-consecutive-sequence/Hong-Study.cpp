class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::set<int> sorts{nums.begin(), nums.end()};
	
	// 개선 필요...
        int maxSequence = 0, sequence = 0, i = -1;
        for (const auto& num : sorts) {
            if (sorts.find(num + 1) != sorts.end()) {
                sequence += 1;
            } else {
                maxSequence = std::max(maxSequence, sequence + 1);
                sequence = 0;
            }
        }

        return maxSequence;
    }
};

