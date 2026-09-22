/**
 * TC : O(n log n)
 *   - 처음에 Arrays.sort() 하는데 O(n log n) 소요. 이하 for loop는 O(n)
 * SC : O(n)
 *   - intervals 배열의 크기 n 만큼 ArrayList 할당하므로 O(n)
 */
class Solution {
    // 정확히 작업 정렬 하는 거랑 비슷한데 그걸 위상정렬이라 하던가.
    // 각 0 번째 인덱스 값으로 정렬되어 있으면
    // 1번째 인덱스 값이 직전 interval[0] <= value <= interval[1] 인 경우에 합쳐진다.
    // 겹치는 값이나 중복 값이 없다는 조건이 없다. 정렬도 보장되어 있지 않다.
    // 하나씩 넣고 구간에 걸치는 경우에 합칠지 버릴지를 결정하면 될 듯 한데, 그걸 어떻게 n^2이 아닌 방식으로 하지
    public int[][] merge(int[][] intervals) {
        List<int[]> answer = new ArrayList<>();
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        int currentStart = intervals[0][0];
        int currentEnd = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {
            int[] pair = intervals[i];

            if (currentEnd >= pair[0]) {
                currentEnd = Math.max(currentEnd, pair[1]);
            } else {
                answer.add(new int[] { currentStart, currentEnd });
                currentStart = pair[0];
                currentEnd = pair[1];
            }
        }
        answer.add(new int[] { currentStart, currentEnd });

        return answer.toArray(new int[0][]);
    }
}
