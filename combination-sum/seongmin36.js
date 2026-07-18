/**
백트래킹(backtracking)을 이용한 풀이

candidates 배열이 순차 정렬을 위해 오름차순으로 정렬한다.
함수 파라미터는 backtracking(남은 수, 현재 push된 배열, 탐색한 인덱스)를 받는다.

동작 원리
1. candidates의 작은 원소부터 하나씩 push하고, 해당 원소를 target에서 차감한다 → remains
2. dfs 방식으로 재귀적으로 호출하여 remains가 0이 되면 최종 result 배열에 push된다.
3. 여기서 breakpoint는 탐색 인덱스의 값이 remains보다 큰 경우이다.
4. 가장 핵심인 부분은 원본 배열에 find_number/remains를 조합할 수 없으면 pop()을 호춣하는데,
이는 진행중인 단계에서 더 이상의 조합을 찾지 못해서 다음 조합을 찾기 위한 필수 과정이다.
 */
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
function combinationSum(candidates, target) {
  let result = [];

  candidates.sort((a, b) => a - b);

  function backtracking(remains, current, index) {
    if (remains === 0) {
      result.push([...current]);
    }

    for (let i = index; i < candidates.length; i++) {
      let find_number = remains - candidates[i];

      if (candidates[i] > remains) break;

      current.push(candidates[i]);
      backtracking(find_number, current, i);
      current.pop();
    }
  }

  backtracking(target, [], 0);

  return result;
}
