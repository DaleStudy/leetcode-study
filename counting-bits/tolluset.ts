/*
 * TC: O(nlogn)
 * SC: O(nlogn)
 * */
function countBits(n: number): number[] {
  return Array.from({ length: n + 1 }, (_, i) => i).map(
    (v) =>
      v
        .toString(2)
        .split("")
        .filter((v) => v === "1").length,
  );
}
