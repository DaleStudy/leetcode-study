class Solution {
    /*
     * 시간복잡도 O(log n)
     */
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length-1;

        while(left<right) {
            int mid =(right - left)/2+left;
            if(nums[right]<nums[mid]) {
                left=mid+1;
            }
            else right=mid;
        }
        return nums[left];
    }
}

