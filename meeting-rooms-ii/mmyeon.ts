/**
 * 접근 방법 :
 *  - 시작 시간과 종료 시간을 각각 배열로 분리한다음 오름차순으로 정렬한다.
 *  - 시작 시간이 가장 빠른 종료 시간보다 빠르다면 다른 회의룸 필요하니까 카운트 증가한다.
 *  - 시작 시간이 종료 시간보다 느리면 회의룸 재사용할 수 있으니까 종료시간 인덱스 증가한다.
 *
 * 시간복잡도 : O(nlogn)
 *  - n = intervals의 길이, 오름차순 정렬
 *
 * 공간복잡도 : O(n)
 * - 인터벌 길이만큼 배열 필요
 */

function minMeetingRooms(intervals: number[][]): number {
  const starts = intervals.map((interval) => interval[0]).sort((a, b) => a - b);
  const ends = intervals.map((interval) => interval[1]).sort((a, b) => a - b);

  let roomCount = 0;
  let endIndex = 0;

  for (let i = 0; i < starts.length; i++) {
    if (starts[i] < ends[endIndex]) roomCount++;
    else endIndex++;
  }

  return roomCount;
}
