import java.util.HashMap;
import java.util.Map;

/**
 본래 brute force로 이중 for문으로 풀었다가 map으로 최적화.
 */
class Solution {
    /**
     * brute force 풀이
     */
//    public int[] twoSumByBruteForce(int[] nums, int target) {
//        for (int i = 0; i < nums.length; i++) {
//            for (int j = i+1; j < nums.length; j++) {
//                if (nums[i] + nums[j] == target) {
//                    return new int[] { i, j };
//                }
//            }
//        }
//        return new int[2];
//    }

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numberMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int required = target - nums[i];
            Integer index = numberMap.get(required);

            if (index != null) {
                return new int[] { index, i };
            }
            numberMap.put(nums[i], i);
        }
        return new int[2];
    }
}