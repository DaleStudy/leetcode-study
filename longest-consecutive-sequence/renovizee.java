import java.util.HashSet;
import java.util.Set;

// tag renovizee 1week unresolved
// https://github.com/DaleStudy/leetcode-study/issues/240
// https://leetcode.com/problems/longest-consecutive-sequence/
class Solution {
    public int longestConsecutive(int[] nums) {
        // 시간복잡도 : O(n)
        // 공간복잡도 : O(n)

        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        int maxCount = 0;
        for (int num : nums) {
            if (numSet.contains(num - 1)) continue;
            int currentCount = 1;
            while (numSet.contains(num + currentCount)) {
                currentCount++;
            }
            maxCount = Math.max(maxCount, currentCount);
        }
        return maxCount;
    }
}


//-------------------------------------------------------------------------------------------------------------
// 기본 문법 피드백
// 1) Set<Integer> numSet = new HashSet<>();
// 2) Math 활용 Math.max(maxCount, currentCount);
//-------------------------------------------------------------------------------------------------------------
