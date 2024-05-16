- https://leetcode.com/problems/meeting-rooms
- https://neetcode.io/problems/meeting-schedule
- time complexity : O(nlogn)
- space complexity : O(n)
- https://algorithm.jonghoonpark.com/2024/05/14/leetcode-252

```java
class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
        intervals = intervals.stream().sorted(Comparator.comparingInt(o -> o.start)).toList();
        for (int i = 0; i < intervals.size() - 1; i++) {
            if(intervals.get(i).end > intervals.get(i+1).start) {
                return false;
            }
        }
        return true;
    }
}
```
