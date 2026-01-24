/**
    최댓값을 기준으로 배열의 합과 1~N까지의 합을 비교하여 확인하는 방식
 */
class Solution {
    public int missingNumber(int[] nums) {
        int max = 0;
        int sum = 0;
        boolean existsZero = false;
        for(int i = 0; i < nums.length; i++) {
            max = Math.max(nums[i], max);
            sum += nums[i];
            if(nums[i] == 0){
                existsZero = true;
            }
        }

        int result = (max * (max + 1)) / 2 - sum;

        if(!existsZero) {
            result = 0;
        } else if(result == 0) {
            result = max + 1;
        }

        return result;
    }
}
