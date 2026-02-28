import java.util.HashSet;

class Solution {
    // This solution was inspired by:
    // https://www.algodale.com/problems/longest-consecutive-sequence/
    //
    // I initially believed this algorithm would run in O(n) time,
    // but it resulted in a Time Limit Exceeded error.
    //
    // Although the expected time complexity is O(n),
    // repeatedly calling set.iterator().next() might introduce overhead.
    // Iterating through the set using a for-loop may be a better approach.
    //
    // In this case, it seems preferable to follow the approach described here:
    // https://www.algodale.com/problems/longest-consecutive-sequence/#%ED%92%80%EC%9D%B4-3

    public int oldApproach(int[] nums) {
        int count = 0;
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        while (set.size() > 0) {
            int buffer = 1;
            // This may cause a Time Limit Exceeded error.
            Integer curr = set.iterator().next();
            set.remove(curr);
            Integer next = curr + 1;
            Integer prev = curr - 1;

            while (set.contains(next)) {
                set.remove(next);
                next++;
                buffer++;
            }

            while (set.contains(prev)) {
                set.remove(prev);
                prev--;
                buffer++;
            }

            count = Math.max(count, buffer);
        }

        return count;
    }

    public int longestConsecutive(int[] nums) {
        int count = 0;

        // The Set has O(n) space complexity,
        // because it may store up to n elements in memory.
        // Is this the correct way to evaluate space complexity?
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        for (int num : set) {
            if (set.contains(num - 1)) {
                continue;
            }

            int currentNum = num;
            int currentCount = 1;

            while (set.contains(currentNum + 1)) {
                currentNum++;
                currentCount++;
            }

            count = Math.max(count, currentCount);
        }

        return count;
    }
}