- 문제: https://leetcode.com/problems/merge-intervals/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/23/leetcode-56

```java
class Solution {
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
}
```

### TC, SC

시간 복잡도는 `O(n*logn)` 공간 복잡도는 `O(n)` 이다. (결과를 반환하기 위해 생성된 `int[][]`는 고려하지 않는다.)
