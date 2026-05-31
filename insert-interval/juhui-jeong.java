/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();

        int newStart = newInterval[0];
        int newEnd = newInterval[1];
        boolean inserted = false;

        for (int i = 0; i < intervals.length; i++) {
            int curStart = intervals[i][0];
            int curEnd = intervals[i][1];

            if (curEnd < newStart) {
                // 1. newInterval 보다 왼쪽
                result.add(new int[]{curStart, curEnd});
            } else if (curStart > newEnd) {
                // 2. newInterval 보다 오른쪽
                if (!inserted) {
                    result.add(new int[]{newStart, newEnd});
                    inserted = true;
                }
                result.add(new int[]{curStart, curEnd});
            } else {
                newStart = Math.min(newStart, curStart);
                newEnd = Math.max(newEnd, curEnd);
            }
        }

        if (!inserted) {
            result.add(new int[]{newStart, newEnd});
        }
        return result.toArray(new int[result.size()][]);
    }
}
