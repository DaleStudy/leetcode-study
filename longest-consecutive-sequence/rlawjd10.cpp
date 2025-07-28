class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> count;
		//  nums에 해당하는 index는 1을 표시
        for (int num: nums) {
            count[num] = 1;
        }

        vector<pair<int, int>> order(count.begin(), count.end());
        sort(order.begin(), order.end(), [](auto& a, auto& b) {return a.first < b.first;});

        int length = 1;
        int currentLength = 1;
        if(order.empty()) return 0;
        for (int i = 1; i < order.size(); i++) {
            // 연속적인지 확인
            if (order[i].first == order[i-1].first +1)
                currentLength++;
            else
                currentLength = 1;
            length = max(length, currentLength);
        }
        
        return length;
    }
};

