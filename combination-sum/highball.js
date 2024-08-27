const combinationSum = function (candidates, target) {
  const result = [];
  const path = [];

  const dfs = function (candidate, residual) {
    if (residual < 0) return;

    path.push(candidate);

    if (residual === 0) {
      result.push([...path]); //그냥 path 넣어주면 뒤에서 path 바뀔 때 result에 들어간 path도 같이 바뀜
      path.pop();
      return;
    }

    for (let i = 0; i < candidates.length; i++) {
      if (candidates[i] >= candidate)
        //작은 애들 빼주는 건 이미 앞에서 했을 것이므로 큰 애들만 빼주면 됨
        dfs(candidates[i], residual - candidates[i]);
    }

    path.pop();
  };

  for (let i = 0; i < candidates.length; i++) {
    //맨 처음에는 candidate이 없기 때문에 초기 조건 세팅할 때 candidate 넣어줘야 함
    dfs(candidates[i], target - candidates[i]);
  }

  return result;
};
