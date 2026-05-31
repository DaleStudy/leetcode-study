class Solution {
public:
    int search(vector<int>& nums, int target) {
        return searchImpl(nums, 0, nums.size() - 1, target);
    }

private:
    int searchImpl(vector<int>& nums, int start, int end, int target)
    {
        if (start > end)
        {
            return -1;
        }

        int mid = (start + end) / 2;
        if (nums[mid] == target)
        {
            return mid;
        }

        if (nums[start] <= nums[mid]) 
        {
            if (nums[start] <= target && nums[mid] >= target) 
            {
                return searchImpl(nums, start, mid - 1, target);
            }

            return searchImpl(nums, mid + 1, end, target);
        }

        if (nums[mid] <= target && nums[end] >= target)
        {
            return searchImpl(nums, mid + 1, end, target);
        }

        return searchImpl(nums, start, mid - 1, target);
    }
};
