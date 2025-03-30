/**
 *@link https://leetcode.com/problems/meeting-rooms/description/
 *
 * 접근 방법 :
 *  - 미팅 시작 시간이 빠른 순으로 정렬
 *  - 현재 미팅 시작 시간이 이전 미팅 끝나는 시간보다 작으면 겹치는 것이므로 false 리턴
 *
 * 시간복잡도 : O(nlogn)
 *  - n = intervals의 길이, 정렬했으므로 O(nlogn)
 *
 * 공간복잡도 : O(1)
 *  - 고정된 변수만 사용
 */

function canAttendMeetings(intervals: number[][]): boolean {
  intervals.sort((a, b) => a[0] - b[0]);

  for (let i = 1; i < intervals.length; i++) {
    const previousMeetingTime = intervals[i - 1];
    const currentMeetingTime = intervals[i];
    if (currentMeetingTime[0] < previousMeetingTime[1]) return false;
  }

  return true;
}
