/**
 * @param strs - 문자열 배열
 * @returns - anagram이 가능한 이중 배열
 * @description
 * - 배열의 길이는 최대 10^4로 순회는 가능한 적게
 * - 문자열의 최대 길이는 100으로 널널
 * - 1. 내부 문자열 정렬 (O(N * K log K))
 * - 2. 아스키로 변환하여 1번만 순회 (O(N * K))
 *
 * - 다만 문자열이 작을 경우 (현재 100 이하로 작은편) 정렬보다 배열 생성과 문자열 join이 더 무거워 질 수 있음
 * - Map을 쓰는게 조금은 더 빠를듯
 */

// function groupAnagrams(strs: string[]): string[][] {
//   const strObj: Record<string, string[]> = {};
//   for (let i = 0; i < strs.length; i++) {
//     const sortedItem = strs[i].split("").sort().join("");
//     strObj[sortedItem] ??= [];
//     strObj[sortedItem].push(strs[i]);
//   }

//   return Object.values(strObj);
// }

function groupAnagrams(strs: string[]): string[][] {
  const strObj: Record<string, string[]> = {};
  for (let i = 0; i < strs.length; i++) {
    const alpha = Array.from({ length: 26 }, () => 0);

    for (const st of strs[i]) {
      alpha[st.charCodeAt(0) - "a".charCodeAt(0)]++;
    }

    const joinStr = alpha.join(",");
    strObj[joinStr] ??= [];
    strObj[joinStr].push(strs[i]);
  }

  return Object.values(strObj);
}

const strs = ["a"];

groupAnagrams(strs);


