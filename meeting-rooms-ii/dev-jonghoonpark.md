- 문제
  - 유료: https://leetcode.com/problems/meeting-rooms-ii/
  - 무료: https://www.lintcode.com/problem/919/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/22/leetcode-253

```java
public class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        intervals = intervals.stream().sorted(Comparator.comparingInt(o -> o.start)).toList();

        List<List<Interval>> days = new ArrayList<>();

        for(Interval interval : intervals) {
            boolean added = false;
            for (List<Interval> day : days) {
                day.add(interval);
                if (canAttendMeetings(day)) {
                    added = true;
                    break;
                }
                day.remove(day.size() - 1);
            }

            if(!added) {
                List<Interval> newDay = new ArrayList<>();
                newDay.add(interval);
                days.add(newDay);
            }
        }

        return days.size();
    }

    public boolean canAttendMeetings(List<Interval> intervals) {
        for (int i = 0; i < intervals.size() - 1; i++) {
            if(intervals.get(i).end > intervals.get(i+1).start) {
                return false;
            }
        }
        return true;
    }
}

class Interval {
    public int start, end;

    public Interval(int start, int end) {
        this.start = start;
        this.end = end;
    }

    @Override
    public String toString() {
        return "{" + start + ", " + end + "}";
    }
}
```

### TC, SC

days의 길이를 m 이라고 했을 때, 시간 복잡도는 `O(n^2 * m)` 공간 복잡도는 `O(n)` 이다. m은 최악의 경우 n이 될 수 있다.
