/*
 * 시간 복잡도: O(nlogn)
 * 공간 복잡도: O(n)
 */
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]);
        });

        List<int[]> merged = new ArrayList<>();
        int[] cur = intervals[0];
        merged.add(cur);

        for (int i = 1; i < intervals.length; i++) {
            int[] next = intervals[i];

            if(cur[1] >= next[0]) {
                cur[1] = Math.max(cur[1], next[1]);
            } else {
                cur = next;
                merged.add(cur);
            }
        }
        return merged.toArray(new int[merged.size()][]);
    }
}
