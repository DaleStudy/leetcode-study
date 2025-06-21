/**
 * <a href="https://leetcode.com/problems/merge-intervals/">week11-4. merge-intervals</a>
 * <li>Description: return an array of the non-overlapping intervals</li>
 * <li>Topics: Array, Sorting                   </li>
 * <li>Time Complexity: O(NlogN), Runtime 10ms  </li>
 * <li>Space Complexity: O(N), Memory 46.18MB   </li>
 */
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (i1, i2) -> i1[0] - i2[0]);

        List<int[]> merge = new ArrayList<>();
        merge.add(intervals[0]);

        for (int i = 1; i < intervals.length; i++) {
            int[] prev = merge.get(merge.size() - 1);
            int[] curr = intervals[i];

            if (curr[0] <= prev[1]) {
                prev[1] = Math.max(prev[1], curr[1]);
            } else {
                merge.add(curr);
            }
        }

        return merge.toArray(new int[merge.size()][]);
    }
}
