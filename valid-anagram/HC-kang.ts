// T.C: O(n)
// S.C: O(1)
function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const NUM_OF_ALPHA = 26;
  const A_CODE = 'a'.charCodeAt(0);
  const bucket = new Array(NUM_OF_ALPHA).fill(0); // S.C: O(1)

  for (let i = 0; i < s.length; i++) { // T.C: O(n)
    bucket[s.charCodeAt(i) - A_CODE]++;
    bucket[t.charCodeAt(i) - A_CODE]--;
  }

  return bucket.every(count => count === 0);
}
