/**
 * <a href="https://leetcode.com/problems/search-in-rotated-sorted-array/">week10-2. search-in-rotated-sorted-array</a>
 * <li>Description: nums is sorted in ascending order and is possibly rotated at an unknown pivot index. return the index of target if it is in nums, or -1 </li>
 * <li>Topics: Array, Binary Search </li>
 * <li>Time Complexity: O(logN), Runtime 1ms      </li>
 * <li>Space Complexity: O(logN), Memory 43.23MB </li>
 */
class Solution {
    public int search(int[] nums, int target) {
        if(nums.length==1) {
            if(nums[0]==target) return 0;
            return -1;
        }

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, nums.length-1});

        int pivot = -1;
        if(nums[0]<nums[nums.length-1]) {
            pivot=nums.length-1;
        }

        while(pivot==-1 && !queue.isEmpty()){
            int[] q = queue.poll();
            int mid = (q[0]+q[1])/2;
            if(mid+1 > nums.length-1) {
                continue;
            }
            if(nums[mid]>nums[mid+1]) {
                pivot=mid;
                break;
            }
            queue.add(new int[]{q[0], mid});
            queue.add(new int[]{mid+1, q[1]});
        }

        int left = 0, right = nums.length-1;
        if(target>=nums[0] && target<=nums[pivot]) {
            right = pivot;
        } else {
            left = pivot+1;
        }


        while(left<=right){
            int mid = (left+right)/2;
            if(target < nums[mid]) {
                right=mid-1;
            } else {
                left=mid+1;
            }
        }

        if(nums[right] == target) {
            return right;
        }

        return -1;
    }
}
