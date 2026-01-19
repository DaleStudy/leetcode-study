/**
 * Missing Number
 * 0부터 n까지의 숫자 중 하나가 빠진 배열에서 누락된 숫자 찾기
 */

// 풀이 1: 합 공식 이용
// 시간복잡도: O(n), 공간복잡도: O(1)
// 0부터 n까지의 합에서 배열 원소들의 합을 빼면 빠진 숫자가 나온다
const missingNumber = (nums) => {
  const n = nums.length;
  const expectedSum = (n * (n + 1)) / 2; // 등차수열 합 공식
  const actualSum = nums.reduce((sum, num) => sum + num, 0);
  return expectedSum - actualSum;
};

// 풀이 2: Set 사용
// 시간복잡도: O(n), 공간복잡도: O(n)
// Set에 넣고 0부터 n까지 순회하면서 없는 숫자 찾기
const missingNumberSet = (nums) => {
  const numSet = new Set(nums);

  for (let i = 0; i <= nums.length; i++) {
    if (!numSet.has(i)) {
      return i;
    }
  }
};
