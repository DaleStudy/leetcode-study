/**
 * https://leetcode.com/problems/counting-bits/submissions/1681218194/
 * @param {number} n
 * @return {number[]}
 */
var countBits = function (n) {
  const ans = [];
  for (let i = 0; i <= n; i++) {
    // Convert i to binary with i.toString(2)
    // Count 1s by splitting into chars, filtering '1', and getting length
    const binary = i.toString(2);
    const onesCount = binary.split('').filter((bit) => bit === '1').length;
    ans.push(onesCount);
  }
  return ans;
};
