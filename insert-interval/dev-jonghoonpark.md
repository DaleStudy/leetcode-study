- 문제: https://leetcode.com/problems/insert-interval/
- 풀이: https://algorithm.jonghoonpark.com/2024/02/14/leetcode-57

## Merge Intervals 문제 답안 응용하기

바로 전에 풀었던 [Merge Intervals](https://algorithm.jonghoonpark.com/2024/07/23/leetcode-56)를 그대로 가져다 쓸 수 있을 것 같아서 해보았더니 통과 된다.

```java
public int[][] insert(int[][] intervals, int[] newInterval) {
    int[][] newIntervals = Arrays.copyOf(intervals, intervals.length + 1);
    newIntervals[intervals.length] = newInterval;
    return merge(newIntervals);
}

public int[][] merge(int[][] intervals) {
    Arrays.sort(intervals, Comparator.comparingInt(o -> o[0]));

    Deque<int[]> intervalDeque = new ArrayDeque<>();
    intervalDeque.add(intervals[0]);
    for(int i = 1; i < intervals.length; i++) {
        int[] lastElement = intervalDeque.getLast();
        int[] nextElement = intervals[i];

        if (lastElement[1] >= nextElement[0]) {
            int[] mergedElement = new int[]{
                    lastElement[0],
                    Math.max(lastElement[1], nextElement[1])
            };
            intervalDeque.removeLast();
            intervalDeque.add(mergedElement);
        } else {
            intervalDeque.add(nextElement);
        }
    }

    return intervalDeque.toArray(int[][]::new);
}
```

### TC, SC

시간 복잡도는 `O(n*logn)` 공간 복잡도는 `O(n)` 이다. (결과를 반환하기 위해 생성된 `int[][]`는 고려하지 않는다.)

## 성능을 개선한 답안 (pointer 사용)

문제를 잘 읽어보면 intervals 의 경우 start를 기준으로 이미 정렬이 되어있다고 하였기 떄문에 따로 정렬을 해줄 필요는 없다.
for loop 에서는 start, end pointer를 이용해서 어느 구간이 병합되는지 기억해두고, 최종적으로 병합을 진행한다.

start 가 -1 인 경우는 맨 오른쪽에 추가가 되어야 한다는 의미이고
end 가 -1 인 경우는 맨 왼쪽에 추가가되어야 한다는 의미이다.
그 외에는 병합이 발생한 것이므로 병합처리를 진행한다.

```java
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int start = -1;
        int end = -1;

        for (int i = 0; i < intervals.length; i++) {
            if (start == -1 && intervals[i][1] >= newInterval[0]) {
                start = i;
            }

            if (newInterval[1] >= intervals[i][0]) {
                end = i;
            }
        }

        if (start == -1) {
            int[][] newIntervals = Arrays.copyOf(intervals, intervals.length + 1);
            newIntervals[intervals.length] = newInterval;
            return newIntervals;
        }

        if (end == -1) {
            int[][] newIntervals = new int[intervals.length + 1][2];
            newIntervals[0] = newInterval;
            System.arraycopy(intervals, 0, newIntervals, 1, newIntervals.length - 1);
            return newIntervals;
        }

        int[][] newIntervals = new int[intervals.length - (end - start)][2];

        if (start >= 0) {
            System.arraycopy(intervals, 0, newIntervals, 0, start);
        }

        newIntervals[start] = new int[]{Math.min(intervals[start][0], newInterval[0]), Math.max(intervals[end][1], newInterval[1])};

        if (intervals.length - (end + 1) >= 0) {
            System.arraycopy(intervals, end + 1, newIntervals, end + 1 - (end - start), intervals.length - (end + 1));
        }

        return newIntervals;
    }
}
```

#### TC, SC

시간 복잡도는 `O(n)` 공간 복잡도는 `O(1)` 이다. (결과를 반환하기 위해 생성된 `int[][]`는 고려하지 않는다.)
