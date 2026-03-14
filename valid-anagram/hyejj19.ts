// 1번째 접근
// 길이가 같지 않다면 무조건 예외이므로 false.
// 두 문자열을 다 Map 으로 만든다.
// 하나의 Map 의 글자와 다른 하나의 Map 에 있는 글자를 비교하며 존재 여부와 카운트 일치 여부를 확인한다.

function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const sMap = new Map();
  for (const sChar of s) {
    sMap.set(sChar, (sMap.get(sChar) || 0) + 1);
  }
  const tMap = new Map();
  for (const tChar of t) {
    tMap.set(tChar, (tMap.get(tChar) || 0) + 1);
  }

  for (const [char, count] of tMap) {
    if (!sMap.get(char)) return false;
    if (sMap.get(char) !== count) return false;
  }

  return true;
}

// 2번째 접근
// Map을 한 개만 만들고도 비교가 가능하지 않을까?
// 1. 하나의 문자열에 대한 Map 을 만든다.
// 2. 나머지 문자열을 순회하며 해당 문자열 카운트를 Map 에서 조회
// 3. 만약 카운트가 0이라면 false
// 4. 조회가 가능하다면 Map 의 카운트를 -1.
function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const sMap = new Map();
  for (const sChar of s) {
    sMap.set(sChar, (sMap.get(sChar) || 0) + 1);
  }
  for (const char of t) {
    const count = sMap.get(char) || 0;
    if (count === 0) return false;
    sMap.set(char, count - 1);
  }

  return true;
}
