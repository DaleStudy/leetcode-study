/**
 * @param s - 문자열 입력값
 * @returns - 부분 문자열 중복없이 가장 긴 문자열의 길이
 * @description
 * - 풀이 1: 앞단계를 Map으로 정리 후 같은 값이 있을 경우 해당 값을 삭제할 때 까지 반복
 * - 삭제 전 길이를 누적해 가장 큰 값을 반환
 *
 * - 풀이 2: 반복을 돌며 찾는게 아닌 해당 idx로 점프하는 과정으로 변경
 * - 최악의 경우를 이전 풀이 1보다 개선
 */

// function lengthOfLongestSubstring(s: string): number {
//   const saveMap: Map<string, boolean> = new Map();
//   const arr = [];
//   for (let i = 0; i < s.length; i++) {
//     if (saveMap.has(s[i])) {
//       for (const key of saveMap.keys()) {
//         arr.push(saveMap.size);
//         saveMap.delete(key);
//         if (key === s[i]) {
//           break;
//         }
//       }
//     }
//     saveMap.set(s[i], true);
//   }

//   arr.push(saveMap.size);

//   return Math.max(...arr);
// }

function lengthOfLongestSubstring(s: string): number {
  const map = new Map<string, number>();

  let maxLength = 0;
  let start = 0;

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    // 해당 문자열이 있고, 그 값이 start 보다 크거나 같을 경우
    // start를 중복 문자 바로 다음 칸으로 이동
    if (map.has(char) && map.get(char)! >= start) {
      start = map.get(char)! + 1;
    }

    map.set(char, i);

    // 현재 idx - 시작점 + 1 === 누적 문자열의 길이
    maxLength = Math.max(maxLength, i - start + 1);
  }

  return maxLength;
}

const s = "dvdf";
lengthOfLongestSubstring(s);


