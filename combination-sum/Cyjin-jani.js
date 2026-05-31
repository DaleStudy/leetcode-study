// ! 나중에 다시 풀어야 할 문제
//! 30분 내에 풀지 못해서 AI의 도움을 받아 구현했습니다..
// recursion의 사용, 종료 조건 등 어느정도 근접한 아이디어를 구현했지만,
// idx를 넘기지 않고 number를 직접 넘기려고 했던 부분이나, results pop을 놓쳤던 부분 등이 있습니다.
const combinationSum = function (candidates, target) {
  const answer = [];

  function recursion(idx, target, results = []) {
    if (target === 0) {
      answer.push([...results]);
      return;
    }
    if (target < 0) return;

    for (let i = idx; i < candidates.length; i++) {
      results.push(candidates[i]);
      recursion(i, target - candidates[i], results);
      results.pop();
    }
  }
  recursion(0, target, []);

  return answer;
};
