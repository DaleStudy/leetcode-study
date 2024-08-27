// Time Complexity: O(nlogn)
// Spatial Complexity: O(nlogn)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        bool found = false;
        vector<pair<int,int>> temp(nums.size());

        for(int i = 0; i < nums.size(); ++i) {
            temp[i] = make_pair(nums[i], i);
        }

        sort(temp.begin(), temp.end());

        int start = 0, end = temp.size() - 1, sum;
        while(start < end) {
            sum = temp[start].first + temp[end].first;

            if (sum == target) {
                break;
            }

            if (sum > target) {
                --end;
            }

            if (sum < target) {
                ++start;
            }
        }

        return vector<int>({temp[start].second, temp[end].second});
    }
};
