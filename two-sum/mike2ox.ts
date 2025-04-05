/**
 * Source: https://leetcode.com/problems/insert-interval/
 * 통과 시간: 10분
 * 풀이방법: Map을 이용하여 필요한 나머지 숫자를 저장하면서 확인
 * 시간복잡도: O(n) - nums 전체를 순회해야함
 * 공간복잡도: O(n)
 */
function twoSum(nums: number[], target: number): number[] {
  // nums의 값을 key로, 인덱스를 value로 저장하는 Map
  const numMap = new Map<number, number>();

  // 입력 배열이 비어있는 경우 빈 배열 반환
  if (nums.length < 2) return [];

  for (let i = 0; i < nums.length; i++) {
    const remain = target - nums[i]; // 필요한 나머지 숫자 계산

    // 필요한 나머지 숫자가 Map에 있는지 체크
    if (numMap.has(remain)) {
      return [numMap.get(remain)!, i];
    }
    // 현재 숫자와 인덱스 저장
    numMap.set(nums[i], i);
  }

  return [];
}
