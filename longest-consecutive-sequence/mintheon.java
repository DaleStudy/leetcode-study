class Solution {
  public int longestConsecutive(int[] nums) {
    Set<Integer> numSet = new HashSet<>();
    int max = 0;

    for(int num : nums) {
      numSet.add(num);
    }

    for(int num : numSet) {
      if(numSet.contains(num - 1)) {
        continue;
      }

      int count = 1;
      int curNum = num;

      while(numSet.contains(curNum + 1)) {
        count++;
        curNum++;
      }

      max = Math.max(max, count);
    }

    return max;
  }
}
