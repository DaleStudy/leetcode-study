class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;

        // 1. nums의 각 원소 count
        for (int num : nums) {
            count[num]++;   // count에 num에 해당하는 value에는 1증가 
        }

        // 2. 많이 나온 순서대로 정렬
        vector<pair<int, int>> freqs(count.begin(), count.end());
        sort(freqs.begin(), freqs.end(), [](pair<int, int> a, pair<int, int> b) {
            return a.second > b.second;  
        });

        // 3. 상위 k개 추출
        vector<int> max(k);
        for (int i = 0; i < k; i++) {
            max[i] = freqs[i].first;
        }

       return max;
    }
};

