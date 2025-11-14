class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> maps;
        for (const auto num : nums) {
            if (maps.find(num) == maps.end())
                maps[num] = 0;
            maps[num] += 1;
        }

        std::vector<std::pair<int, int>> sorts{maps.begin(), maps.end()};
        sort(sorts.begin(), sorts.end(),
             [](std::pair<int, int> a, std::pair<int, int> b) {
                 return a.second > b.second;
             });

        std::vector<int> result;
        int i = 0;
        for (const auto m : sorts) {
            result.push_back(m.first);
            i++;
            if (i == k)
                break;
        }

        return result;
    }
};

