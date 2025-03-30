/*
# Time Complexity: O(n)
# Space Complexity: O(1)
*/
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        ArrayList<int[]> answer = new ArrayList<>();

        int i = 0;
        int n = intervals.length;

        // newInterval보다 왼쪽의 구간들 추가
        while (i < n && intervals[i][1] < newInterval[0]) {
            answer.add(intervals[i]);
            i++;
        }

        // newInterval과 겹치는 구간들 병합
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        answer.add(newInterval);

        // newInterval보다 오른쪽의 구간들 추가
        while (i < n) {
            answer.add(intervals[i]);
            i++;
        }

        return answer.toArray(new int[answer.size()][]);
    }
}
