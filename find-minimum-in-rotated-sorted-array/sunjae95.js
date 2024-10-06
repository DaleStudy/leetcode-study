/**
 * @description
 * brainstorming:
 * brute force
 *
 * n = length of head
 * time complexity: O(n)
 * space complexity: O(1)
 */
var findMin = function (nums) {
  let answer = 5000;
  nums.forEach((num) => (answer = Math.min(answer, num)));

  return answer;
};

/* n = length of head
 * time complexity: O(n)
 * space complexity: O(1)
 */
var findMin = function (nums) {
  let answer = nums[0];
  if (nums.length === 1) return answer;
  if (answer < nums[nums.length - 1]) return answer;

  for (let i = nums.length - 1; i >= 0; i--) {
    if (answer < nums[i]) return answer;
    answer = nums[i];
  }

  return answer;
};
