/**
 * 주어진 배열에서 합이 target이 되는 모든 조합 찾기
 * 문제 특징: 같은 숫자를 여러 번 사용 가능
 *
 * 백트래킹 알고리즘: 모든 가능성을 시도해보다가, 해결책이 아닌 경우 이전 단계로 되돌아가 다른 경로를 탐색
 * 시간복잡도: O(N^T) (N: candidates 배열의 길이, T: target)
 */

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  const result = [];

  /**
   * start: 현재 탐색을 시작할 배열의 인덱스
   * target: 남은 목표 합계
   * currCombination: 현재까지 선택한 숫자들의 배열
   */
  const backtrack = (start, target, currCombination) => {
    if (target === 0) {
      // target을 정확히 맞춘 경우(target이 0인 경우) result에 추가
      result.push([...currCombination]);
      return;
    }
    if (target < 0) {
      // target이 0보다 작은 경우 빠른 종료
      return;
    }
    for (let i = start; i < candidates.length; i++) {
      currCombination.push(candidates[i]); // 현재 숫자 추가
      backtrack(i, target - candidates[i], currCombination); // 재귀 호출로 다음단계 진행
      currCombination.pop(); // 현재 숫자 제거 (백트래킹) 후 다음 숫자 탐색
    }
  };
  backtrack(0, target, []); // 초기 호출(백트래킹 시작)
  return result;
};
