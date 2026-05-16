// Time Complexity: O(n)
// Space Complexity: O(1)

const missingNumber = (nums) => {
  const n = nums.length;
  const total = (n * (n + 1)) / 2; // 가우스 공식
  const sum = nums.reduce((acc, cur) => acc + cur, 0);
  return total - sum;
};
