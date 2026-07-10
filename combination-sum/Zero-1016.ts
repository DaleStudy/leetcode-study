/**
 * Combination Sum1 (같은 숫자 재사용 가능) — 비효율 버전
 *
 * 표기:
 *   n = candidates 길이
 *   T = target
 *   M = candidates 중 최솟값
 *   D = T / M (재귀 트리의 최대 깊이)
 * 시간 복잡도: O(nᴰ × D)
 *   - start 인덱스가 없어 매번 0부터 탐색 → [2,2,3], [2,3,2], [3,2,2] 같은
 *     순열을 전부 방문 (조합 하나당 최대 D! 개)
 *   - 정답 발견 시 경로 복사 O(D), 후처리(sort + join + Set) 비용은 탐색량에 묻힘
 *
 * 공간 복잡도: O(D! × 정답 개수 × D)
 *   - 중복 조합이 제거 전까지 combinations에 전부 쌓임 → OOM 위험
 *   - 재귀 스택: O(D)
 */
function combinationSum1(candidates: number[], target: number): number[][] {
  const combinations: number[][] = [];

  const backtrack = (currentPath: number[], currentSum: number) => {
    const pathCopy = [...currentPath];
    const remainingTarget = target - currentSum;

    if (remainingTarget === 0) {
      combinations.push(pathCopy);
    }

    for (let i = 0; i < candidates.length; i++) {
      const candidate = candidates[i];

      if (remainingTarget - candidate >= 0) {
        pathCopy.push(candidate);
        backtrack(pathCopy, currentSum + candidate);
        pathCopy.pop();
      }
    }
  };

  backtrack([], 0);

  // 중복 조합 제거 후 반환
  return [...new Set(combinations.map((path) => path.sort().join(",")))].map(
    (str) => str.split(",").map(Number),
  );
}

/**
 * Combination Sum2 (같은 숫자 재사용 가능) — 최적화 버전
 *
 * 표기:
 *   n = candidates 길이
 *   T = target
 *   M = candidates 중 최솟값
 *   D = T / M (재귀 트리의 최대 깊이)
 *
 * 시간 복잡도: O(nᴰ × D)
 *   - Big-O 상한은 1번과 같지만 실제 탐색량은 훨씬 작음:
 *     1) start 인덱스 → 순열 중복 탐색 원천 차단 (조합당 정확히 1회 방문)
 *     2) 정렬 + break → 무효한 가지를 통째로 절단
 *   - 정렬 비용 O(n log n)은 지수 항에 묻힘
 *
 * 공간 복잡도: O(D + 정답 개수 × D)
 *   - 재귀 스택 + 공유 path: O(D)
 *   - 출력 배열: 정답 개수 × 평균 길이 (출력 자체라 최소 비용)
 */
function combinationSum2(candidates: number[], target: number): number[][] {
  const combinations: number[][] = [];
  candidates.sort((a, b) => a - b);

  const backtrack = (start: number, path: number[], remaining: number) => {
    if (remaining === 0) {
      combinations.push([...path]);
      return;
    }

    for (let i = start; i < candidates.length; i++) {
      if (candidates[i] > remaining) break;

      path.push(candidates[i]);
      backtrack(i, path, remaining - candidates[i]);
      path.pop();
    }
  };

  backtrack(0, [], target);
  return combinations;
}
