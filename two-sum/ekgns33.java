import java.util.HashMap;
import java.util.Map;

/*
input : array of integers, single integer target
output : indices of the two numbers that they add up to target
constraint:
1) is integer positive? 
no [-10^9, 10^9]
2) is there any duplicates?
yes. but only one valid answer exists
3) can i reuse elem?
no

sol1) brute force
nested for loop. tc: O(n^2), sc: O(1) when n is the length of input

sol2) better solution with hash map
iterate through the array
  check if target - current elem exists
    if return pair of indices
    else save current elem and continue

tc : O(n), sc: O(n) when n is the length of input

 */
class Solution {
  public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> prev = new HashMap<>();
    for(int i = 0; i < nums.length; i++) {
      int key = target - nums[i];
      if(prev.containsKey(key)) {
        return new int[] {prev.get(key), i};
      }
      prev.put(nums[i], i);
    }
    return null;
  }
}
