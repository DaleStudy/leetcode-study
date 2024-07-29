- 문제: https://leetcode.com/problems/non-overlapping-intervals/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/23/leetcode-435

```java
public int eraseOverlapIntervals(int[][] intervals) {
    int overlappingCount = 0;
    Arrays.sort(intervals, Comparator.comparingInt(o -> o[1]));

    int currentEnd = intervals[0][1];
    for (int i = 0; i < intervals.length - 1; i++) {
        // overlapping 이 발생된 경우
        if (currentEnd > intervals[i + 1][0]) {
            overlappingCount++;

            // 앞 interval 의 end 값이 뒤 interval 의 end 보다 작을 경우 이전 pointer 유지
            if (currentEnd < intervals[i + 1][1]) {
                continue;
            }
        }

        currentEnd = intervals[i + 1][1];
    }

    return overlappingCount;
}
```

### TC, SC

시간 복잡도는 `O(n*logn)` 공간 복잡도는 `O(1)` 이다.
