// Time complexity: O(n^2)
// Space complexity: O(n)

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
  let answer = nums[0];

  const productGroups = [[]];

  for (let i = 0; i < nums.length; i++) {
    const productGroup = productGroups.at(-1);

    if (nums[i] === 0) {
      productGroups.push([]);
    }

    if (productGroup.length === 0) {
      productGroup.push(nums[i]);
      continue;
    }

    productGroup.push(nums[i] * productGroup.at(-1));
  }

  for (const group of productGroups) {
    for (let i = 0; i < group.length; i++) {
      answer = Math.max(answer, group[i]);

      for (let j = 0; j < i; j++) {
        answer = Math.max(answer, group[i] / group[j]);
      }
    }
  }

  return answer;
};
