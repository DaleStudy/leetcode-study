import java.util.HashSet;
import java.util.Set;

class Solution {
  public int longestConsecutive(int[] nums) {
    Set<Integer> numSet = new HashSet<>();

    for(int num : nums) {
      numSet.add(num);
    }

    int longestSize = 0;

    for(int num : numSet) {
      if(!numSet.contains(num - 1)) {
        int current = num;
        int count = 1;

        while(numSet.contains(current + 1)) {
          count++;
          current++;
        }

        longestSize = Math.max(count, longestSize);
      }
    }

    return longestSize;
  }
}
