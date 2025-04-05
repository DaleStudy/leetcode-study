/**
 *
 * 접근 방법 :
 *  - 정렬 사용하지 않고 o(n)을 풀기 위해서 숫자 빈도수를 배열 인덱스로 저장
 *  - 숫자 빈도스를 맵에 저장
 *  - 맵을 순회하면서, 빈도수를 배열에 저장 (동일 반도수 처리하기 위해서 2차원 배열 사용)
 *  - 배열을 역순으로 순회하면서 빈도수 기반의 값을 결과 배열에 저장
 *  - 결과 배열을 k개만큼 잘라서 리턴
 *
 * 시간복잡도 : O(n)
 *  - nums 배열 1회 순회하면서 맵에 저장하니까 O(n)
 *
 * 공간복잡도 : O(n)
 *  - nums 배열 길이만큼 맵과 2차원 배열에 정리하니까 O(n)
 */
function topKFrequent(nums: number[], k: number): number[] {
  const numMap = new Map();

  for (const num of nums) {
    numMap.set(num, (numMap.get(num) ?? 0) + 1);
  }

  const storedArr: number[][] = Array(nums.length + 1)
    .fill(null)
    .map(() => []);

  for (const [num, frequency] of numMap) {
    storedArr[frequency].push(num);
  }

  const result: number[] = [];

  for (let i = storedArr.length - 1; i >= 0; i--) {
    if (storedArr[i].length > 0) result.push(...storedArr[i]);
  }

  return result.slice(0, k);
}
