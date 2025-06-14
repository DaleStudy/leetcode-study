public class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> output = new ArrayList<>();

        Arrays.sort(intervals, (a, b) -> a[0]- b[0]);

        for (int[] interval : intervals) {
            if (output.isEmpty() || output.get(output.size() - 1)[1] < interval[0]) {
                output.add(interval);
            } else {
                output.get(output.size() - 1)[1] = Math.max(output.get(output.size() - 1)[1], interval[1]);
            }
        }

        return output.toArray(new int[output.size()][]);
    }
}

