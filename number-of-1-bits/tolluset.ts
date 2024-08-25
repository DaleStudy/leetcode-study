/*
 * TC: O(logn)
 * SC: O(logn)
 * */
function hammingWeight(n: number): number {
  return n
    .toString(2)
    .split("")
    .filter((s) => s === "1").length;
}
