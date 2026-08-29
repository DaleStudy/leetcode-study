import java.util.*;

class Solution {
    public int maxSubArray(int[] nums) {
        int answer = Integer.MIN_VALUE;

        int[] arr = new int[nums.length + 1];
        
        for(int i = 0 ; i < nums.length ; i++){
            arr[i + 1] = Math.max(arr[i] + nums[i], nums[i]);
            answer = Math.max(answer, arr[i + 1]);
        }
        
        return answer;
    }
}
