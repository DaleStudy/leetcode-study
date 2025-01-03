import java.util.HashMap;
import java.util.Map;

class Solution {
  /**
   공간복잡도: O(n)
   시간복잡도: O(n)
   */

  public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> numMap = new HashMap<>();

    for(int i = 0; i < nums.length; i++) {
      numMap.put(nums[i], i);
    }

    for(int i = 0; i < nums.length; i++) {
      int pairNum = target - nums[i];
      if(numMap.containsKey(pairNum) && numMap.get(pairNum) != i) {
        return new int[]{i, numMap.get(target - nums[i])};
      }
    }

    return new int[2];
  }
}
