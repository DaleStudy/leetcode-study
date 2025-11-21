/**
각 문자열을 순회하며, 글자별로 등장한 횟수를 비교할 수 있을 듯 하다.
s 를 먼저 순회하여 생성한 map 에 대해 t 를 순회하며 map 을 소거시켜보자

시간 복잡도: O(n)
공간 복잡도: O(log n) (문자열 수를 기준)
 */

function isAnagram(s: string, t: string): boolean {
  const wordMap = new Map<string, number>();
  for (let i = 0; i < s.length; i++) {
    const value = wordMap.get(s[i])
    if (value) {
      wordMap.set(s[i], value + 1);
    } else {
      wordMap.set(s[i], 1);
    }
  }

  for (let i = 0; i < t.length; i++) {
    const remainWord = wordMap.get(t[i]);
    if (remainWord) {

      if (remainWord > 1) {
        wordMap.set(t[i], remainWord - 1);
      } else if (remainWord === 1) {
        wordMap.delete(t[i]);
      }
    } else {
      return false;
    }
  }

  return wordMap.size === 0 ? true : false;
}
