class Solution {
    public int search(int[] nums, int target) {
        int firstIdx = binarySearch(nums);
        int result = 0;
        if (firstIdx == 0) {
            return binarySearch(target, nums, 0, nums.length - 1);
        } else if (target >= nums[0]) {
            return binarySearch(target, nums, 0, firstIdx);
        } else {
            return binarySearch(target, nums, firstIdx, nums.length - 1);
        }
    }

    public int binarySearch(int[] nums) {
            int start = 0;
            int end = nums.length -1;
            while(start < end) {
                int mid = (start + end) / 2;
                if(nums[mid] < nums[end]) {
                    end = mid;
                } else {
                    start = mid + 1;
                }
            }
            return start;
    }

    public int binarySearch(int target, int[] nums, int start, int end) {
            int result = -1;
            while(start <= end) {
                int mid = (start + end) / 2;
                if(nums[mid] > target) {
                    end = mid - 1;
                } else if(nums[mid] < target){
                    start = mid + 1;
                } else {
                    result = mid;
                    break;
                }
            }

            return result;
    }
        
    
}
