/**
 * 새로운 interval을 기존 intervals 배열에 삽입하고 겹치는 구간을 병합하여 반환하는 함수
 * @param {number[][]} intervals - 기존 interval 배열
 * @param {number[]} newInterval - 추가하려는 interval
 * @returns {number[][]} - 새로운 interval을 추가하고 병합한 배열
 * 
 * 시간복잡도 : O(n)
 *   - intervals 배열을 순회하면서 newInterval과 겹치는 구간을 찾아 병합
 * 
 * 공간복잡도 : O(n)
 *   - 결과를 저장하기 위한 배열을 생성.
 */
function insert(intervals: number[][], newInterval: number[]): number[][] {
  // 결과 배열을 newInterval 하나만 가진 배열로 시작
  const result: number[][] = [newInterval];
  
  for (let i = 0; i < intervals.length; i++) {
    const newItem = intervals[i];
    const lastItem = result.pop()!;
    
    // 현재 구간이 lastItem 구간의 왼쪽에 완전히 위치하는 경우
    if (newItem[1] < lastItem[0]) {
      result.push(newItem);
      result.push(lastItem);
    }
    // 현재 구간이 lastItem 구간의 오른쪽에 완전히 위치하는 경우
    else if (newItem[0] > lastItem[1]) {
      result.push(lastItem);
      result.push(newItem);
    }
    // 두 구간이 겹치는 경우: 병합하여 하나의 구간으로 병합
    else {
      lastItem[0] = Math.min(lastItem[0], newItem[0]);
      lastItem[1] = Math.max(lastItem[1], newItem[1]);
      result.push(lastItem);
    }
  }
  
  return result;
}

