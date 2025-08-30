/**
 * 문제 유형
 * - String
 *
 * 문제 설명
 * - 애너그램 그룹화
 *
 * 아이디어
 * 1) 각 문자열을 정렬하여 키로 사용하고 그 키에 해당하는 문자열 배열을 만들어 리턴
 *
 */
function groupAnagrams(strs: string[]): string[][] {
  const map = new Map<string, string[]>();

  for (let i = 0; i < strs.length; i++) {
    const key = strs[i].split("").sort().join("");
    map.set(key, [...(map.get(key) ?? []), strs[i]]);
  }
  return [...map.values()];
}
