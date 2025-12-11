/**
3글자씩으로 구성된 각 문자열 배열을 순회하며, 각 문자열을 알파벳 순서로 정렬한 순서를 기준으로
동일하다면 원래의 문자열을 key 로 하는 해시에 포함시켜보자

시간 복잡도: O(n log n) 공간 복잡도: O(n) 정도 나오지 않을까?
 */
function groupAnagrams(strs: string[]): string[][] {
  const anaMap = new Map<string, string[]>();

  for (let i = 0; i < strs.length; i++) {
    const hashKey = strs[i].split("").sort().join("");

    const arr = anaMap.get(hashKey);
    if (!arr) {
      anaMap.set(hashKey, [strs[i]]);
    } else {
      anaMap.set(hashKey, [...arr, strs[i]]);
    }
  }

  return [...anaMap.values()];
}
