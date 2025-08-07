import java.util.*;

class Solution {
/* 시간 복잡도: O(N), nums.length를 n이라고 할 때, 시간 복잡도는 O(N)
 * - for 루프: O(N)
 * - HashMap 연산 (containsKey, put): 평균 O(1)
 * 
 * 공간 복잡도: O(N), HashMap에 최대 n개의 요소를 저장할 수 있음
 */ 
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numToIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int remains = target - nums[i];
            if (numToIndex.containsKey(remains)) {
                return new int[]{i, numToIndex.get(remains)};
            }
            numToIndex.put(nums[i], i);
        }
        return null;
    }
}

