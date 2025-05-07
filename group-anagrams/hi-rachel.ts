// TC O(N * K log K), N: 단어 수, K: 평균 단어 길이, 각 단어를 정렬
// SC O(N * K)

/**
 * Array.from() => 이터러블 -> 일반 배열로 변환
 */
function groupAnagrams(strs: string[]): string[][] {
  const anagramMap: Map<string, string[]> = new Map();

  for (const word of strs) {
    const key = word.split("").sort().join("");
    const group = anagramMap.get(key) || [];
    group.push(word);
    anagramMap.set(key, group);
  }
  return Array.from(anagramMap.values());
}

/**
 * reduce 풀이
 */
// function groupAnagrams(strs: string[]): string[][] {
//   const anagramMap = strs.reduce((map, word) => {
//     const key = word.split("").sort().join("");
//     if (!map.has(key)) {
//       map.set(key, []);
//     }
//     map.get(key).push(word);
//     return map;
//   }, new Map<string, string[]>());

//   return Array.from(anagramMap.values());
// }

/**  간결한 버전
 * x ||= y (ES2021)
 * x가 falsy 값이면 y를 할당
 * JS에서 falsy 값 = false, 0, '', null, undefined, NaN
 *
 * Object.values() => 객체의 값들만 배열로 추출할때 사용
 */
// function groupAnagrams(strs: string[]): string[][] {
//     const anagramMap: {[key: string]: string[]} = {};

//     strs.forEach((word) => {
//         const key = word.split('').sort().join('');
//         (anagramMap[key] ||= []).push(word);
//     });

//     return Object.values(anagramMap);
// }
