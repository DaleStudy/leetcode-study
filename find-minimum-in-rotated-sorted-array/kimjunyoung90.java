// 요구사항 : 이진 탐색 이용
class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        while(left < right) {
            int mid = (left + right) / 2;
            //중앙 값이 오른쪽 값보다 크다. = 최소값이 오른쪽 구간에 있음
            if(nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return nums[left];
    }
}
