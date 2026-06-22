/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const r = Array.from(nums.length);
  const l = Array.from(nums.length);
  const a = Array.from(nums.length);
  for (let i = 0; i < nums.length; i++) {
    const temp = r[i - 1] ?? 1;
    const temp2 = nums[i - 1] ?? 1;
    r[i] = temp * temp2;
  }
  for (let i = nums.length - 1; i > -1; i--) {
    const temp = l[i + 1] ?? 1;
    const temp2 = nums[i + 1] ?? 1;
    l[i] = temp * temp2;
  }
  for (let i = 0; i < nums.length; i++) {
    a[i] = l[i] * r[i];
  }

  return a;
};
