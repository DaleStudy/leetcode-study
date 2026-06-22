function lengthOfLongestSubstring(s: string): number {
  if (s.length <= 1) return s.length;

  let left = 0;
  let right = 0;
  let maxLen = -1;
  const sMap = new Map();
  while (right !== s.length) {
    const curS = s[right];
    // Map에 존재하지 않는다 -> 중복 X -> right 전진
    if (!sMap.get(curS)) {
      sMap.set(s[right], 1);
      right++;
    } else {
      // Map에 존재 한다 -> 중복 O -> left 전진
      while (left <= right && sMap.get(curS)) {
        sMap.set(s[left], sMap.get(s[left]) - 1);
        left++;
      }
    }
    maxLen = Math.max(maxLen, right - left);
  }
  return maxLen;
}
