/**
 * 문제 설명
 * - 주어진 회의시간을 진행할 수 있는 최소의 회의시간 갯수 구하기
 *
 * 아이디어
 * 1) minheap + greeday
 *   - 회의시간 시작시간으로 정렬(회의 일정을 시간 순으로 처리)
 *   - Heap에는 현재 사용 중인 회의실의 종료 시간들만 저장
 *       - 회의 시작시간이 끝시간보다 같거나 크면 회의실 쓸수 있는 거니까 shift 해서 회의 꺼냄
 *       - 회의시간 끝 시간을 힙에 넣고, 끝시간 오름차순으로 정렬(minheap)
 *   - 최종적으로 heap의 크기 = 필요한 회의실 개수
 */

type Interval = { start: number; end: number };

class Solution {
  minMeetingRooms(intervals: Interval[]): number {
    if (intervals.length === 0) return 0;

    intervals.sort((a, b) => a.start - b.start);

    const heap: number[] = [];

    for (const interval of intervals) {
      const { start, end } = interval;

      if (heap.length > 0 && heap[0] <= start) {
        heap.shift();
      }

      heap.push(end);
      heap.sort((a, b) => a - b);
    }

    return heap.length;
  }
}
