/**
 *
 * 접근 방법 :
 *  - 중복 숫자 제거하고 빠르게 조회하기 위해서 Set 사용
 *  - 연속된 숫자의 시작점(현재 숫자보다 작은 숫자가 없는 경우)를 찾아서 연속된 길이 카운트
 *  - 최대 길이 갱신
 *
 * 시간복잡도 : O(n)
 *  - Set 생성, 숫자 탐색 모두 O(n)
 *
 * 공간복잡도 : O(n)
 *  - 최악의 경우, nums 배열 크기만큼 set에 저장하니까 O(n)
 */
function longestConsecutive(nums: number[]): number {
  const numSet = new Set(nums);
  let longestLength = 0;

  for (const num of numSet) {
    if (!numSet.has(num - 1)) {
      let currentLength = 1;
      let currentNum = num + 1;

      while (numSet.has(currentNum)) {
        currentLength++;
        currentNum++;
      }

      longestLength = Math.max(longestLength, currentLength);
    }
  }

  return longestLength;
}
