package week01.longest_consecutive_sequence;

import java.util.HashMap;
import java.util.Map;

class Solution {

    public boolean containsDuplicate(int[] nums) {

        Map<Integer, Integer> countMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            countMap.put(nums[i], countMap.getOrDefault(nums[i] , 0) + 1);
        }

        for (Map.Entry<Integer, Integer> map : countMap.entrySet()) {
            if (map.getValue() >= 2) {
                return true;
            }
        }

        return false;
    }
}
