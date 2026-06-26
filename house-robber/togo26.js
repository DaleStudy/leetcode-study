/**
 * @param {number[]} nums
 * @return {number}
 */
/*
TC: O(n)
SC: O(n)
*/
var rob = function (nums) {
  const pocket = {};

  for (let i = 0; i < nums.length; i++) {
    if (i === 0) {
      pocket[i] = nums[i];
      continue;
    }
    if (i === 1) {
      pocket[i] = Math.max(nums[i - 1], nums[i]);
      continue;
    }

    pocket[i] = Math.max(pocket[i - 2] + nums[i], pocket[i - 1]);
  }

  return Object.values(pocket).reduce((acc, cur) => Math.max(acc, cur), 0);
};

/*
TC: O(n)
SC: O(1) -> variable used
*/
var rob = function (nums) {
  let prev2 = 0;
  let prev1 = 0;

  for (let i = 0; i < nums.length; i++) {
    let temp = prev1;
    prev1 = Math.max(prev2 + nums[i], prev1);
    prev2 = temp;
  }

  return prev1;
};
