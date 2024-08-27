// Time Complexity: O(n)
// Spatial Complexity: O(n);

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
