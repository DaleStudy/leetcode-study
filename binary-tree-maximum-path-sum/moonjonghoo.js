var maxPathSum = function (root) {
  let maxSum = -Infinity;

  function dfs(node) {
    if (node === null) return 0; // 6) Base Case
    const left = Math.max(dfs(node.left), 0); // 8) Pruning
    const right = Math.max(dfs(node.right), 0); // 8) Pruning

    const currentSum = left + node.val + right; // 9) Pivot Sum
    maxSum = Math.max(maxSum, currentSum); // 7) Global Max

    return node.val + Math.max(left, right); // 10) Return Value
  }

  dfs(root); // 4) DFS 시작
  console.log(maxSum); // 최종 답 출력
};
