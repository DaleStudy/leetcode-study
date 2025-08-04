import java.util.List;
import java.util.PriorityQueue;

/**
 * Definition of Interval:
 * public class Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

public class Solution {
    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
    // 시간복잡도: O(n log n)
    public int minMeetingRooms(List<Interval> intervals) {

        if (intervals == null || intervals.isEmpty()) {
            return 0;
        }

        // 주어진 시간 인터벌 리스트를 시작 시간 기준으로 정렬
        intervals.sort((i1, i2) -> i1.start - i2.start);

        // PriorityQueue 선언: 시간 interval의 end time 기준
        PriorityQueue<Interval> meetingRooms = new PriorityQueue<>((i1, i2) -> i1.end - i2.end);

        for (Interval interval : intervals) {

            // 최초 meeting room 
            if (meetingRooms.isEmpty()) {
                meetingRooms.offer(interval);
                continue;
            }

            Interval meeting = meetingRooms.peek();
            // (0, 8), (8, 10) is not conflict at 8
            if (meeting.end <= interval.start) {
                // 앞의 회의 종료되었으므로 회의실 재사용
                meetingRooms.poll();
            }
            // 새 회의실 추가
            meetingRooms.offer(interval);
        }

        return meetingRooms.size();

    }
}

