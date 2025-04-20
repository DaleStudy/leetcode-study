function combinationSum(candidates, target) {
  const result = [];

  // 1. 정렬: 가지치기를 위한 필수
  candidates.sort((a, b) => a - b);

  function backtrack(startIndex, path, remaining) {
    if (remaining === 0) {
      result.push([...path]);
      return;
    }

    for (let i = startIndex; i < candidates.length; i++) {
      const current = candidates[i];

      // 2. 가지치기
      if (current > remaining) break;

      // 3. 현재 값 선택
      path.push(current);
      backtrack(i, path, remaining - current); // i로 재귀 호출: 같은 수 중복 사용 가능
      path.pop(); // 4. 백트래킹
    }
  }

  backtrack(0, [], target);
  return result;
}
