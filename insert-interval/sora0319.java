public class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> list = new ArrayList<>();

        int order = 0;
        while (order < intervals.length && intervals[order][0] < newInterval[0]) {
            list.add(intervals[order]);
            order++;
        }
        list.add(newInterval);
        while (order < intervals.length) {
            list.add(intervals[order]);
            order++;
        }

        List<int[]> output = new ArrayList<>();
        output.add(list.get(0));

        for (int i = 1; i < list.size(); i++) {
            int[] last = output.get(output.size() - 1);
            int[] current = list.get(i);
            if (last[1] < current[0]) {
                output.add(current);
            } else {
                last[1] = Math.max(last[1], current[1]);
            }
        }

        return output.toArray(new int[output.size()][]);
    }
}

