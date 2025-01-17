// Time complexity: O(1)
// Space complexity: O(1)

/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
  const stack = [];
  let current = n;

  for (let i = 0; i < 32; i++) {
    stack.push(current % 2);
    current = Math.floor(current / 2);
  }

  let answer = 0;

  for (let i = 0; i < 32; i++) {
    const popped = stack.pop();
    answer += popped * 2 ** i;
  }

  return answer;
};
