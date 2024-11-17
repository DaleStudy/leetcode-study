/**
 * @description
 *
 * n = length of n
 * time complexity: O(n)
 * space complexity: O(n)
 */
var reverseBits = function (n) {
  let answer = 0;
  let binary = n.toString(2);

  if (binary.length < 32) binary = "0".repeat(32 - binary.length) + binary;

  for (let i = binary.length - 1; i >= 0; i--)
    answer += Math.pow(2, i) * Number(binary[i]);

  return answer;
};
