class Solution {
    /* 시간 복잡도: O(N)
    * - for 루프: O(N)
    * 공간 복잡도: O(N), answer 배열
    */ 
    public int[] productExceptSelf(int[] nums) {
        int product = 1;
        int zeroCnt = 0;
        for (int num : nums) {
            if (num == 0) {
                zeroCnt += 1;
                continue;
            }
         product *= num;
        }

        int[] answer = new int[nums.length];
        if (zeroCnt > 1) {
            return answer;
        }

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (zeroCnt == 1) {
                if (num == 0) answer[i] = product;
            } else {
                answer[i] = product / num;
            }
        }
        return answer;
    }
}

