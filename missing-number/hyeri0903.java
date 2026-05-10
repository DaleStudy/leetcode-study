class Solution {
    public int missingNumber(int[] nums) {
        /**
        1.distinc number 로 이루어진 0~n 까지의 배열 중 missing number return
        2.constraints
        - n 최소 = 1, 최대 = 10000
        - 배열길이 min=0, max=n
        3.solutions
        - sorting 하고 for문으로 missing num check. time: O(n log n), space: O(1)
        - 전체 sum - 실제 sum
         */

         Arrays.sort(nums);
         int n = nums.length;
         int answer = 0;
         int i = 0;

         for(i = 0; i < n; i++) {
            if(nums[i] != i) {
                answer = i;
                return answer;
            }
         }
         if(i == n) {
            answer = n;
            return answer;
         }
         return answer;
    }
}
