// time complexity: O(n);
// 특정 nums[i] 가 target이 되기위한 보수 (target - nums[i])를 candidate Map에서 찾으면 종료

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> candidate = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {

            int diff = target - nums[i];

            if(candidate.containsKey(diff)) {
                return new int[] { candidate.get(diff), i };
            }

            candidate.put(nums[i], i);
        }
        return new int[0];
    }
}
