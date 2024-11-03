import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

class Solution {

  public int[][] merge(int[][] intervals) {
    // TC: O(N log N)
    // SC: O(N)

    // length가 2보다 적으면 그대로 반환
    if (intervals.length < 2) {
      return intervals;
    }

    List<int[]> output = new ArrayList<>();

    // intervals 배열을 시작 시간 기준으로 정렬
    Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));

    for (int[] interval : intervals) {
      // output이 비어있거나, 현재 interval이 마지막에 추가된 구간과 겹치지 않으면 추가
      if (output.isEmpty() || output.get(output.size() - 1)[1] < interval[0]) {
        output.add(interval);
      } else {
        // 겹치는 경우, 마지막 구간의 끝 시간을 업데이트
        output.get(output.size() - 1)[1] = Math.max(output.get(output.size() - 1)[1], interval[1]);
      }
    }

    // List<int[]>를 int[][] 배열로 변환하여 반환
    return output.toArray(new int[output.size()][]);
  }
}
