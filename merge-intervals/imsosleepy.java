// 정렬을 하지 않으려면 O(N^2)이 걸림
// 정렬을 나면 아무리 빨라도 O(N log N)이지만 이후에 문제가 간단해짐
// currentEnd >= nextStart → 겹치면 end 값을 업데이트 하는 간단한 방식으로 구현
class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) return intervals;

        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        List<int[]> merged = new ArrayList<>();
        int[] currentInterval = intervals[0];
        merged.add(currentInterval);

        for (int[] interval : intervals) {
            int currentEnd = currentInterval[1]; 
            int nextStart = interval[0];
            int nextEnd = interval[1];

            if (currentEnd >= nextStart) {
                // 겹치면 end 값을 업데이트
                currentInterval[1] = Math.max(currentEnd, nextEnd);
            } else {
                // 겹치지 않으면 새로운 구간으로 추가
                currentInterval = interval;
                merged.add(currentInterval);
            }
        }

        return merged.toArray(new int[merged.size()][]);
    }
}
