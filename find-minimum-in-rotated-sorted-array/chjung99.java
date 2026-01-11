class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int mid = (left + right) / 2;
        while (left + 1 < right){
            mid = (left + right) / 2;
            if (nums[mid] > nums[right]) {
                left = mid;
            }
            if (nums[mid] < nums[right]) {
                right = mid;
            }
        }
        mid = (left + right) / 2;
        if (nums[mid] > nums[right]) return nums[right];
        else {
            return nums[mid];
        }
    }
}


