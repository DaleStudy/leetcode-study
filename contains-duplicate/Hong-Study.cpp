class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> map;
        for(const auto& num: nums){
            if(map.find(num) != map.end()){
                return true;
            }

            map[num] = 1;
        }

        return false;
    }
};

