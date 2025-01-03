/*
 * T.C: O(n) -> 배열 nums를 한 번 순회
 * S.C: O(n) → 최대 n개의 요소가 저장됨
 */
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> map = new HashMap<>();
        for  (int i = 0; i < nums.length; i++) {
            int k = target - nums[i];

            if (map.containsKey(k)) {
                return new int[] { map.get(k), i };
            }

            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("exception handling for java compilation");
        
    }
}

