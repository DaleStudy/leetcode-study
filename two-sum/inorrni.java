/**
 *    모르겠다..
 *    1. nums 배열 순회
 *        - i + j == target
 *            1) 이중 반복문 사용 sum = i+j
 *            2) sum이 target과 일치하는가
 *            3) true 면 break
 *        - target - i == j
 *            뭔가 될 것 같은데..
 *    2. 이중 반복문 외 방법
 *        - ,,? 공부하자
 */

class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length - 1; i++) {
            for(int j = i+1; j < nums.length; j++) {
                if (target - nums[i] == nums[j]) {
                    return new int[] {i, j};
                }
            }
        }
        return null;
    }
}

