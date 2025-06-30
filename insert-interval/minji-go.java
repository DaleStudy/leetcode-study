/**
 * <a href="https://leetcode.com/problems/insert-interval/">week13-3. insert-interval</a>
 * <li>Description: Return intervals after the insertion of 'new interval' given an array of non-overlapping intervals</li>
 * <li>Topics: Array </li>
 * <li>Time Complexity: O(N), Runtime 1ms       </li>
 * <li>Space Complexity: O(N), Memory 45.02MB   </li>
 */
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> answer = new ArrayList<>();

        int i = 0;
        while (i < intervals.length && intervals[i][1] < newInterval[0]) {
            answer.add(intervals[i++]);
        }

        while (i < intervals.length && newInterval[1] >= intervals[i][0]) {
            newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
            newInterval[1] = Math.max(intervals[i][1], newInterval[1]);
            i++;
        }
        answer.add(newInterval);

        while (i < intervals.length) {
            answer.add(intervals[i++]);
        }

        return answer.toArray(new int[answer.size()][]);
    }
}
