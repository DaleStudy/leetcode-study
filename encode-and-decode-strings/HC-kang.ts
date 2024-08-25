/**
 * The most simple way
 */
function encode(strs: string[]): string {
	return strs.join('🏖️');
};
function decode(s: string): string[] {
	return s.split('🏖️');
};

// T.C: O(n)
// S.C: O(n)
function encode(strs: string[]): string {
  return strs.map((s) => s.length + '#' + s).join('');
}

// T.C: O(n)
// S.C: O(n)
function decode(s: string): string[] {
  const res: string[] = [];
  let curIdx = 0;
  while (curIdx < s.length) {
    const sepIdx = s.indexOf('#', curIdx);
    const len = parseInt(s.slice(curIdx, sepIdx), 10);
    res.push(s.slice(sepIdx + 1, sepIdx + 1 + len));
    curIdx = sepIdx + 1 + len;
  }
  return res;
}
