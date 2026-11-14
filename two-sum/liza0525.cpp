// TC: O(n) - 최대 nums의 길이만큼 시간이 소요
// SC: O(n) - idx_map에 최대 nums의 길이 만큼 저장
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> idx_map;

        for (int i=0; i < int(nums.size()); i++){
            int other_num = target - nums[i];

            // lookup을 한 번만 하기 위해 find로 iterator 찾아두기
            auto it = idx_map.find(other_num);

            if (it != idx_map.end()) {
                return {i, it->second};
            }

            idx_map[nums[i]] = i;
        }
        return {};
    }
};
