//time-complexity : O(n)
//space-complexity : O(1)

const missingNumber = function (nums) {
  const sum = nums.reduce((acc, cur) => acc + cur);
  const n = nums.length;
  return (n * (n + 1)) / 2 - sum;
};
