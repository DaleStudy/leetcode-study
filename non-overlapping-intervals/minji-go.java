/**
 * <a href="https://leetcode.com/problems/non-overlapping-intervals/">week12-3. non-overlapping-intervals</a>
 * <li>Description: return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping</li>
 * <li>Topics: Array, Dynamic Programming, Greedy, Sorting  </li>
 * <li>Time Complexity: O(N), Runtime 45ms                  </li>
 * <li>Space Complexity: O(1), Memory 73.45MB               </li>
 * <li>Note : refer to the answer                           </li>
 */
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (i1, i2) -> i1[1] - i2[1]);

        int skip = 0;
        int end = Integer.MIN_VALUE;

        for (int[] interval : intervals) {
            if (interval[0] < end) {
                skip++;
            } else {
                end = interval[1];
            }
        }

        return skip;
    }
}
