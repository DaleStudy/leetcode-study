/**
 * 문제 설명
 * - 주어진 문자열 s에서 주어진 문자열 t의 모든 문자를 포함하는 최소 윈도우를 찾는 문제
 *
 * 아이디어
 * - 슬라이딩 윈도우 + 해시맵(need, window)을 이용하여 풀이한다.
 * - 오른쪽 포인터를 먼저 이동하고, 이미 모두 포함되어 있는 경우 왼쪽 포인터를 이동하여 최소 윈도우를 찾는다.
 *
 */
function minWindow(s: string, t: string): string {
  if (t.length > s.length) return "";

  const need = new Map<string, number>();
  const window = new Map<string, number>();

  for (const char of t) {
    need.set(char, (need.get(char) || 0) + 1);
  }

  let have = 0;
  let needSize = need.size;
  let res = [-1, -1];
  let resLen = Infinity;

  let left = 0;

  for (let right = 0; right < s.length; right++) {
    const c = s[right];
    window.set(c, (window.get(c) || 0) + 1);

    if (need.has(c) && window.get(c) === need.get(c)) {
      have++;
    }

    while (have === needSize) {
      const currentResLen = right - left + 1;
      if (currentResLen < resLen) {
        res = [left, right];
        resLen = currentResLen;
      }

      const lChar = s[left];
      window.set(lChar, window.get(lChar)! - 1);

      if (need.has(lChar) && window.get(lChar)! < need.get(lChar)!) {
        have--;
      }
      left++;
    }
  }

  const [start, end] = res;
  return resLen === Infinity ? "" : s.slice(start, end + 1);
}
