import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, List<Integer>> map = new HashMap();
        for (int i = 0; i < nums.length; i++) {
            if (!map.containsKey(nums[i])) {
                map.put(nums[i], new ArrayList<Integer>());
            }
            map.get(nums[i]).add(i);
        }

        for (Map.Entry<Integer, List<Integer>> e: map.entrySet()) {
            int other = target - e.getKey();
            if (map.containsKey(other)) {
                if (e.getKey() == other && map.get(other).size() > 1) {
                    return new int[]{e.getValue().get(0), e.getValue().get(1)};
                }
                return new int[]{e.getValue().get(0), map.get(other).get(0)};
            }
        }
        return new int[]{};
    }
}

