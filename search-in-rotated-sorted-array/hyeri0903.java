class Solution {
    public int search(int[] nums, int target) {
        /**
        1.prob: index k기준으로 left rotated 된 array 에서 target index return, 존재하지 않으면 -1 return
        2.constraints
        - asc 정렬된 배열, 모두 unique 한 값
        - 반드시 O(log n) 으로 풀 것
        - num.length min=1, max = 5000
        3.solution
        - bruteforce, for문 -> time: O(n)
        - binary search -> time: O(log n), space: O(1)
         */

        int n = nums.length;
        int left = 0, right = n - 1;
        

        while(left <= right) {
            int mid = (left + right) / 2;
            
            //target 찾으면 index return
            if(nums[mid] == target) {
                return mid;
            }

            if(nums[left] <= nums[mid]) {
                //왼쪽이 정렬된 경우
                if(nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                //오른쪽이 정렬된 경우
                if(nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
}
