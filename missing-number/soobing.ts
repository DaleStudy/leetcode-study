/**
 * 문제 설명
 * - 0부터 n까지 숫자가 중복 없이 단 하나만 빠져있는 숫자 찾기
 *
 * 아이디어
 * 1) 체크 배열 생성
 * - 0부터 n까지 숫자가 중복 없이 단 하나만 빠져있는 숫자 찾기
 *
 * 2) 수학적 접근
 * - n*(n+1)/2: 배열의 합 - 주어진 배열의 합 = 빠진 숫자
 *
 * 3) XOR 활용
 * - 0 ^ 1 ^ 2 ^ ... ^ n : 모든 숫자 XOR
 * - nums[0] ^ nums[1] ^ ... ^ nums[n-1] : 배열 내 존재하는 숫자들 XOR
 * - 이 둘을 XOR하면, 중복되는 숫자는 모두 상쇄되어 빠진 숫자만 남음.
 */

function missingNumber(nums: number[]): number {
  const check = new Array(nums.length).fill(false);

  nums.forEach((num) => (check[num] = true));

  for (let i = 0; i < nums.length; i++) {
    if (!check[i]) return i;
  }
  return nums.length;
}

// 수학적 접근
function missingNumber2(nums: number[]): number {
  const n = nums.length;
  const expectedSum = (n * (n + 1)) / 2;
  const actualSum = nums.reduce((acc, cur) => acc + cur, 0);
  return expectedSum - actualSum;
}

// XOR 활용
function missingNumber3(nums: number[]): number {
  let xor = 0;
  for (let i = 0; i < nums.length; i++) {
    xor ^= i ^ nums[i];
  }

  return xor ^ nums.length;
}
