// tc: O(1) -> 32비트로 고정되어있어 1로 봄..
// sc: O(1)
const reverseBits = function (n) {
  const binaryStr = n.toString(2).padStart(32, '0');
  const answer = binaryStr.split('').reverse().join('');
  return parseInt(answer, 2);
};
