// Time Complexity: O(n^target);
//    - target에 비례하는 tree 깊이에 따라 n번 순회 발생
// Spatial Complexity: O(target);
//    - target에 비례하는 visited vector, answer vector만 있으면 됨.

class Solution {
public:
  vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> ans;
    vector<int> visited;
    backtrack(ans, candidates, visited, target, 0);
    return ans;
  }

  void backtrack(
    vector<vector<int>>& ans, 
    vector<int>& candidates, 
    vector<int>& visited,
    int target,
    int prev
  ) {
    if(target == 0) {
      ans.push_back(visited);
      return;
    }

    for(int i = prev; i < candidates.size(); ++i) {
      if (target - candidates[i] < 0) {
        continue;
      }

      visited.push_back(candidates[i]);
      backtrack(ans, candidates, visited, target - candidates[i], i);
      visited.pop_back();
    }
  }
};
