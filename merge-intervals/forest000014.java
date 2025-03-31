/*
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
*/

class Solution {
    public int[][] merge(int[][] intervals) {
        int n = intervals.length;

        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        ArrayList<int[]> ans = new ArrayList<>();
        ans.add(new int[2]);
        ans.get(0)[0] = intervals[0][0];
        ans.get(0)[1] = intervals[0][1];

        for (int i = 1; i < n; i++) {
            if (ans.get(ans.size() - 1)[1] < intervals[i][0]) {
                ans.add(new int[2]);
                ans.get(ans.size() - 1)[0] = intervals[i][0];
                ans.get(ans.size() - 1)[1] = intervals[i][1];
            } else {
                ans.get(ans.size() - 1)[1] = Math.max(ans.get(ans.size() - 1)[1], intervals[i][1]);
            }
        }

        return ans.toArray(new int[ans.size()][]);
    }
}
