/*
 * 첫번쨰 풀이: 각 단어마다 이전에 처리한 단어들과 일일이 비교하여 애너그램 여부 확인
 * 첫번째 풀이로도 통과는 함
 * 시간복잡도: O(n²*k), 공간복잡도: O(n*k) (n: 단어 수, k: 평균 단어 길이)
 */
/*var groupAnagrams = function (strs) {
  if (strs.length === 1) return [strs];

  const answer = [[strs[0]]];

  for (let i = 1; i < strs.length; i++) {
    let flag = false;
    for (let k = 0; k < answer.length; k++) {
      const word = answer[k][0];
      if (isAnagram(word, strs[i])) {
        answer[k].push(strs[i]);
        flag = true;
      }
    }
    if (!flag) answer.push([strs[i]]);
  }

  return answer;
};

var isAnagram = function (s1, s2) {
  if (s1.length !== s2.length) return false;

  // 영어 소문자 개수 총 26개
  const code = new Array(26).fill(0);

  for (let i = 0; i < s1.length; i++) {
    code[s1[i].charCodeAt() - 97]++;
    code[s2[i].charCodeAt() - 97]--;
  }
  return code.every((x) => x === 0);
};
*/
///////////////////////////////////////////////////////////////

/*
 * 두번쨰 풀이: 정렬된 문자열을 키로 사용하여 해시맵에 그룹화
 * 시간복잡도: O(n*k*log(k)), 공간복잡도: O(n*k) (n: 단어 수, k: 평균 단어 길이)
 */
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  if (strs.length === 1) return [strs];

  // 해시맵으로 애너그램 그룹 관리
  const answer = {};

  for (let i = 0; i < strs.length; i++) {
    // 애너그램은 정렬하면 동일한 문자열이 됨
    // k는 최대 100으로 제한되어 있어 정렬(O(k log k))이 효율적이므로
    // 첫 번째 풀이의 카운팅 방식 대신 간단히 정렬로 판별 가능
    const sort = [...strs[i]].sort().join("");

    // 이미 같은 키가 있으면 해당 그룹에 추가
    if (sort in answer) {
      answer[sort].push(strs[i]);
    } else {
      // 새로운 그룹 생성
      answer[sort] = [strs[i]];
    }
  }

  return Object.values(answer);
};
