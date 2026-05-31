/**
 *
 * SC: O(n)
 * TC: O(n)
 */
const missingNumber = function (nums) {
  const n = nums.length;
  const range_min = 0;
  const range_max = n;
  const numsMap = new Set();

  for (let num of nums) {
    numsMap.add(num);
  }

  for (let i = range_min; i <= range_max; i++) {
    if (!numsMap.has(i)) return i;
  }
};

// 위 풀이의 경우 공간복잡도가 O(1)이 되지 않음.
// 아래의 경우가 공간복잡도 O(1)이 되는 풀이.
// 가우스 합 공식 이용. n개의 숫자에서 0부터 n까지의 합에서 실제 배열의 합을 빼면 누락된 숫자가 나옴.
const missingNumber_v2 = function (nums) {
  const n = nums.length;
  const expectedSum = (n * (n + 1)) / 2;
  const actualSum = nums.reduce((acc, num) => acc + num, 0);
  return expectedSum - actualSum;
};
