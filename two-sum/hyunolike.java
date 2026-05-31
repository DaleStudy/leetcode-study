class Solution {
    public int[] twoSum(int[] nums, int target) {
        // 모든 경우의 수 체크

        // 결과값 
        int[] result = null;

        // 순회
        for(int i = 0; i < nums.length; i++){
            for(int j = i+1; j < nums.length; j++) {
                int sum = nums[i] + nums[j];
                if(sum == target) {
                    result = new int[]{i, j};
                }
            }
        }

        return result;
    }
}
