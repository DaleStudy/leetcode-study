// 1번 풀이
function lengthOfLongestSubstring1(s: string): number {
  let seen = new Set<string>();
  let start = 0;
  let maxLength = 0;

  for (let end = 0; end < s.length; end++) {
    const char = s[end];

    // 중복된 문자가 나오면 Set에서 제거하면서 start를 앞으로 이동
    while (seen.has(char)) {
      seen.delete(s[start]);
      start++;
    }

    // 중복이 없으면 현재 윈도우 길이 갱신
    seen.add(char);
    maxLength = Math.max(maxLength, end - start + 1);
  }

  return maxLength;
}

// 2번 풀이
function lengthOfLongestSubstring2(s: string): number {
  let substring = "";
  let maxLength = 0;

  for (let i = 0; i < s.length; i++) {
    const char = s[i];

    // 중복 문자가 있다면, 그 문자 이후부터 잘라냄
    if (substring.includes(char)) {
      const index = substring.indexOf(char);
      substring = substring.slice(index + 1);
    }

    substring += char;
    maxLength = Math.max(maxLength, substring.length);
  }

  return maxLength;
}
