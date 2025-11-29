/**
 * @param {number} n
 * @return {number}
 */
const hammingWeight = (n) => {
  const binaryString = n.toString(2);
  let oneCount = 0;

  for (const bit of binaryString) {
    if (bit === '1') {
      oneCount += 1;
    }
  }

  return oneCount;
};

// 다른 풀이
// const hammingWeight = (n) => {
//   return n.toString(2).split('1').length - 1;
// };
