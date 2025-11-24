/*
시간 복잡도: O(n²)
공간 복잡도: O(n)
*/
function topKFrequent(nums: number[], k: number): number[] {
  const map = new Map<number, number>();
  let numLength: number[] = nums;
  let mapArray;

  while (numLength.length > 0) {
    // 현재 기준 숫자
    const current = numLength[0];
    // 갯수 확인
    const elementNum = numLength.filter((n) => n === current);
    // 확인한 숫자 제거
    const filteredNum = numLength.filter((n) => n !== current);

    numLength = filteredNum;
    map.set(current, elementNum.length);
  }
  mapArray = [...map];
  mapArray.sort((a, b) => b[1] - a[1]);

  // 상위 k개 num만 반환
  return mapArray.slice(0, k).map(([num, _]) => num);
}
