/**
 * @param {number} n
 * @return {number}
 */
const hammingWeight = (n) => {
  const binary = n.toString(2);
  return binary.split("").filter((bit) => bit === "1").length;
};
