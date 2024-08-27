/**
 * @description
 * brainstorming:
 * recursive function
 *
 * time complexity: O(n)
 * space complexity: O(n)
 */
var productExceptSelf = function (nums) {
  const answer = Array.from({ length: nums.length }, () => 0);

  const search = (left, right, i) => {
    if (i === nums.length - 1) {
      answer[i] = left * right;
      return nums[i];
    }

    const productLeft = left * nums[i];
    const productRight = search(productLeft, right, i + 1);

    answer[i] = left * productRight;

    return productRight * nums[i];
  };

  search(1, 1, 0);

  return answer;
};
