/**
 *
 * 접근 방법 :
 *  - group anagrams 저장할 map 선언하기
 *  - 단어 문자열 strs 순회하면서 단어 정렬하기
 *  - map에 존재하지 않는 경우, 배열 형태로 맵에 저장하기.
 *  - map에 존재하는 경우, 기존 값에 현재 단어 추가하기
 *  - map의 값들만 리턴하기
 *
 * 시간복잡도 : O(n * klogk)
 *  - n은 strs 길이, k는 단어 길이
 *  - strs 배열 n번 순회 : O(n)
 *  - 각 단어 정렬 : O(klogk)
 *
 * 공간복잡도 : O(n)
 *  - map에 strs 길이만큼 저장하니까
 */
function groupAnagrams(strs: string[]): string[][] {
  const map = new Map<string, string[]>();

  for (const str of strs) {
    const sortedWord = str.split("").sort().join("");
    if (map.get(sortedWord)) {
      map.get(sortedWord)!.push(str);
    } else {
      map.set(sortedWord, [str]);
    }
  }

  return [...map.values()];
}
