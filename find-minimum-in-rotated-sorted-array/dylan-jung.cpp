class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0; int r = nums.size() - 1;
        int min = -10000;
        if(nums[l] <= nums[r]) return nums[0]; // ordered case
        while(l <= r) {
            int mid = (l+r)/2;
            if(nums[l] > nums[mid]) {
                min = mid;
                r = mid;
            }
            else if(nums[mid] > nums[r]) {
                min = mid+1;
                l = mid+1;
            }
            else {
                break;
            }
        }
        return nums[min];
    }
};
