/*
* 조건
* 문자열은 영어 소문자
* 서로 anagram이 되는 쌍을 배열로 묶어서 리턴
* 자기 자신은 anagram 혼자서 가능함
* return 하는 배열 순서는 관계없음

* 아이디어
* strs를 돌면서 str에 어떤 알파벳이 몇개씩 있는지를 계산한다
* 알파벳 개수가 같은 문자열끼리 몹는다
*/
function groupAnagrams(strs: string[]): string[][] {
  const anagramMap = new Map<string, string[]>();

  for (const str of strs) {
    const sortedStr = generateAnagramKey2(str);
    if (!anagramMap.has(sortedStr)) {
      anagramMap.set(sortedStr, []);
    }

    anagramMap.get(sortedStr)!.push(str);
  }

  return Array.from(anagramMap.values());
}
// TC: O(N * M)
// SC: O(N * M)

function generateAnagramKey1(str: string): string {
  return str.split("").sort().join("");
}
// TC: O(NlogN)
// SC: O(N)

function generateAnagramKey2(str: string): string {
  let count = new Array(26).fill(0);

  for (let c of str) {
    count[c.charCodeAt(0) - "a".charCodeAt(0)]++;
  }

  return count.join("-");
}
// TC: O(N)
// SC: O(1)
