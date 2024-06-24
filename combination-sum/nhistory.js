var combinationSum = function (candidates, target) {
  let output = [];

  // Helper function for depth-first search
  const dfs = (index, currentVal, arr) => {
    // If the remaining value is less than 0, no need to proceed further
    if (currentVal < 0) return;
    // If we have found a valid combination
    if (currentVal === 0) {
      output.push([...arr]);
      return;
    }

    // Iterate over the candidates starting from the current index
    for (let i = index; i < candidates.length; i++) {
      arr.push(candidates[i]);
      dfs(i, currentVal - candidates[i], arr);
      arr.pop(); // backtrack
    }
  };

  // Start DFS with the initial target and empty combination
  dfs(0, target, []);

  return output;
};
