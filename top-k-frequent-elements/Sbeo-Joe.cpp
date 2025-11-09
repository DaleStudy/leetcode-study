class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // value, count
        unordered_map<int, int> um;
        for(auto& n : nums){
            um[n]++;
        }

        //value, count
        vector<std::pair<int, int>> vec(um.begin(), um.end());
        sort(vec.begin(), vec.end(), 
            [](const auto& a, const auto& b) { return a.second > b.second;});

        vector<int> ret;
        for(int i=0; i< k; i++){
            ret.push_back(vec[i].first);
        }

        return ret;
    }
};
