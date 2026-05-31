// class Solution {
// public:
//     vector<vector<int>> threeSum(vector<int>& nums) {
//         set<vector<int>> ans;
//         map<int, int> counter; // {num : cnt}
//         vector<int> targets;
//         int target, left, right;
        
//         for(int i = 0; i < nums.size(); i++)
//             counter[nums[i]]++;
        
//         for(auto iter : counter)
//             targets.push_back(iter.first);

//         for(int i = 0; i < targets.size(); i++) {
//             target = -1 * targets[i];
            
//             vector<int> new_nums;
//             counter[targets[i]]--;
//             for(auto iter : counter) {
//                 for(int j = 0; j < iter.second; j++)
//                     new_nums.push_back(iter.first);
//             }
//             left = 0; right = new_nums.size() - 1;
//             while(left < right) {
//                 int sum = new_nums[left] + new_nums[right];
//                 if(sum == target && targets[i] <= new_nums[left] && new_nums[left] <= new_nums[right])
//                     ans.insert(vector<int>({targets[i], new_nums[left], new_nums[right]}));
            
//                 if(sum < target)
//                     left++;
//                 else
//                     right--;
//             }
//             counter[targets[i]]++;
//         }
        
//         return vector<vector<int>> (ans.begin(), ans.end());
//     }
// };

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        int left, right, sum;

        sort(nums.begin(), nums.end());

        for(int i = 0; i < nums.size(); i++) {
            if(i > 0 && nums[i] == nums[i - 1])
                continue;

            left = i + 1; right = nums.size() - 1;
            while(left < right) {
                sum = nums[i] + nums[left] + nums[right];
                if(sum == 0) {
                    ans.push_back(vector<int> ({nums[i], nums[left], nums[right]}));
                    left++; right--;
                    while(left < right && nums[left] == nums[left - 1])
                        left++;
                    while(left < right && nums[right] == nums[right + 1])
                        right--;
                }
                else if(sum < 0)
                    left++;
                else if(sum > 0)
                    right--;
            }
        }

        return ans;
    }
};

