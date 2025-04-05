import java.util.HashMap;
import java.util.Map;

class Solution {
  public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> indexMap = new HashMap<>();

    for(int i = 0; i < nums.length; i++) {
      int remain = target - nums[i];

      if(indexMap.containsKey(remain)) {
        return new int[] {i, indexMap.get(remain)};
      }

      indexMap.put(nums[i], i);
    }

    return new int[]{};
  }
}
