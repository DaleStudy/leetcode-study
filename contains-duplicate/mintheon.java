import java.util.HashSet;
import java.util.Set;

class Solution {
  public boolean containsDuplicate(int[] nums) {
    Set<Integer> numSet = new HashSet();

    for(int num : nums) {
      numSet.add(num);
    }

    return numSet.size() != nums.length;
  }
}
