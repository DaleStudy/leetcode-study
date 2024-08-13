/*
 * TC: O(n)
 * SC: O(n)
 * */
function countSubstrings(s: string): number {
  const t = "#" + s.split("").join("#") + "#";
  const n = t.length;
  const p = new Array(n).fill(0);
  let center = 0,
    right = 0,
    l = 0;

  const mirror = (i: number, p: number[], c: number, r: number) => {
    return Math.min(r - i, p[c * 2 - i]);
  };

  const isRightBound = (i: number, p: number[], n: number) => {
    return i + p[i] + 1 < n;
  };

  const isLeftBound = (i: number, p: number[]) => {
    return i - p[i] - 1 >= 0;
  };

  const isPalindrome = (i: number, p: number[], t: string) => {
    return t[i + p[i] + 1] === t[i - p[i] - 1];
  };

  const isLongest = (i: number, p: number[], r: number) => {
    return i + p[i] > r;
  };

  const calcTotal = (i: number, p: number[]) => {
    return Math.floor((p[i] + 1) / 2);
  };

  for (let i = 0; i < n; i++) {
    if (i < right) {
      p[i] = mirror(i, p, center, right);
    }

    while (
      isRightBound(i, p, n) &&
      isLeftBound(i, p) &&
      isPalindrome(i, p, t)
    ) {
      p[i]++;
    }

    if (isLongest(i, p, right)) {
      center = i;
      right = i + p[i];
    }

    l += calcTotal(i, p);
  }

  return l;
}
