/*
 * TC: O(n)
 * SC: O(n)
 * */
function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) {
    return false;
  }

  const groupS = groupBy(s);
  const groupT = groupBy(t);

  return Object.keys(groupS).every((k) => groupS[k] === groupT[k]);
}

const groupBy = (v: string) =>
  v.split("").reduce((acc, cur) => ((acc[cur] = (acc[cur] ?? 0) + 1), acc), {});
