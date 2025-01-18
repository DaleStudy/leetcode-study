/**
 * https://leetcode.com/problems/group-anagrams/description/
 * Runtime: 27ms, Memory: 64.26MB
 *
 * Time Complexity: O(n * m * log m)
 * Space Complexity: O(n * m)
 *
 * 접근
 * anagrams 관계인 단어는 정렬 시 모두 동일한 단어가 된다.
 * 그러므로 정렬된 단어가 key 값이 되고, str을 정렬했을 때 key값과 동일한 경우 value가 되도록 추가.
 */

function groupAnagrams(strs: string[]): string[][] {
  let answer = [];
  const anagramMap = new Map<string, string[]>();

  for (let str of strs) {
    const key = str.split("").sort().join(""); // O(m * log m)
    if (!anagramMap.has(key)) {
      anagramMap.set(key, []);
    }
    anagramMap.get(key)?.push(str);
  }

  anagramMap.forEach((value) => {
    answer.push(value);
  });

  return answer;
}

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]);
