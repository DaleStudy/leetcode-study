// class Solution {
// public:
//     int findMin(vector<int>& nums) {
//         queue<pair<int, int>> que;
//         int left = 0, right = nums.size() - 1, mid, previous, next;

//         if(nums.size() == 1)
//             return nums[0];
//         if(nums.size() == 2)
//             return min(nums[0], nums[1]);

//         que.push({left, right});
//         while(!que.empty()) {
//             left = que.front().first;
//             right = que.front().second;
//             que.pop();

//             mid = (left + right) / 2;
//             previous = (mid == 0 ? nums.size() - 1 : mid - 1);
//             next = (mid + 1 == nums.size() ? 0 : mid + 1);

//             if(nums[previous] > nums[mid] && nums[mid] < nums[next])
//                 return nums[mid];
            
//             if(left <= mid - 1)
//                 que.push({left, mid - 1});
//             if(mid + 1 <= right)
//                 que.push({mid + 1, right});
//         }

//         return -1;
//     }
// };

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size() - 1, mid;

        while(left < right) {
            mid = (left + right) / 2;

            if(nums[right] < nums[mid])
                left = mid + 1;
            else
                right = mid;
        }

        return nums[left];
    }
};

