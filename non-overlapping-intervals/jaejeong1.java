import java.util.Arrays;
import java.util.Comparator;

class Solution {
  public int eraseOverlapIntervals(int[][] intervals) {
    // 풀이: 정렬 후 각 구간의 끝 값을 저장해가며 양 옆을 비교, 제거 대상일때 카운트를 증가시켜 반환한다.
    // TC: O(N)
    // SC: O(1)

    // intervals를 각 구간의 끝 값을 기준으로 정렬
    Arrays.sort(intervals, Comparator.comparingInt(a -> a[1]));

    int answer = 0;
    int end = intervals[0][1]; // 첫 번째 구간의 끝 값

    // 두 번째 구간부터 순회하며 겹치는지 확인
    for (int i = 1; i < intervals.length; i++) {
      if (intervals[i][0] < end) { // 현재 구간이 이전 구간과 겹치면
        answer++; // 제거 횟수를 증가
      } else {
        end = intervals[i][1]; // 겹치지 않으면 현재 구간의 끝 값을 갱신
      }
    }

    return answer;
  }
}
