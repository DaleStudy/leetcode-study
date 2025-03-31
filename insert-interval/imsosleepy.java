// start와 end라는 두개의 변수를 이용하면 한번만 순회해도 가능하다.
// 조건이 세개 밖에 없어서 단순하게 시뮬레이션 하면된다.
// (1) 현재 구간이 newInterval보다 앞에 있음 → 그대로 추가
// (2) 현재 구간이 newInterval보다 뒤에 있음 → 병합할 필요 없음, 바로 추가
// (3) 겹치는 경우 병합
// 마지막 newInterval 추가 (병합된 상태일 수도 있음) << 이걸 못찾아서 너무 오래걸림
// 시간복잡도 O(N)
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        int n = intervals.length;
        int start = newInterval[0];
        int end = newInterval[1];

        for (int i = 0; i < n; i++) {
            
            if (intervals[i][1] < start) {
                result.add(intervals[i]);
            } 
            
            else if (intervals[i][0] > end) {
                result.add(new int[]{start, end});
                start = intervals[i][0];  // 기존 구간부터 다시 추가
                end = intervals[i][1];
            } 
            
            else {
                start = Math.min(start, intervals[i][0]);
                end = Math.max(end, intervals[i][1]);
            }
        }
        
        result.add(new int[]{start, end});

        return result.toArray(new int[result.size()][]);
    }
}
