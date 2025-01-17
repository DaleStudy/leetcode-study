import java.util.HashSet;

class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> mySet = new HashSet<Integer>();

        for (int num : nums) {
            mySet.add(num);
        }

        int result = 0;
        for (int num : mySet) {
            int cnt = 1;
            if (!mySet.contains(num - 1)) {
                while (mySet.contains(++num)) {
                    ++cnt;
                }
                result = Math.max(cnt, result);
            }
        }
        return result;
    }
}
