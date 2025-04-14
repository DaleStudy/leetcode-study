
// NOTE: 카데인 알고리즘.
// TODO: O(n^2) 복잡도의 브루트포스 방식으로도 풀어보기.
class Solution {
    public int maxSubArray(int[] nums) {

        int maxSum = nums[0];
        int curSum = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            curSum = Math.max(nums[i], curSum + nums[i]);  
            maxSum = Math.max(maxSum, curSum);             
        }
        
        return maxSum;
    }
}

// NOTE: 시작점 변경의 조건(?)을 제대로 정의하지 못해 틀린문제..
// 답지 보고 해결....
class WrongSolution {
    public int maxSubArray(int[] nums) {
        int gMax = -123456789; 
        int curMax = -123456789;
        int curSum = 0;

        for(int i = 0; i < nums.length; i++) {
            if(curMax < nums[i]) {
                // 시작점 변경.
                curSum = nums[i];
                curMax = nums[i];
            } else {
                curSum += nums[i];
                curMax = Math.max(curMax, curSum);
            }

            gMax = Math.max(gMax, curMax);
        }

        return gMax;
    }
   
}
