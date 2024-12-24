import java.util.ArrayList;
import java.util.List;

/**
 input : array of distinct integers, single integer target
 output : all unique combinations of candidates where chosen ones sum is target
 constraints:
 1) can we use same integer multiple times?
 yes
 2) input array can be empty?
 no. [1, 30]


 solution 1)
 combination >> back-tracking
 O(2^n) at most 2^30 << (2^10)^3 ~= 10^9

 tc : O(2^n) sc : O(n) call stack
 */
class Solution {
  public List<List<Integer>> combinationSum(int[] candidates, int target) {
    List<List<Integer>> answer = new ArrayList<>();
    List<Integer> prev = new ArrayList<>();
    backTrackingHelper(answer, prev, candidates, target, 0, 0);
    return answer;
  }
  private void backTrackingHelper(List<List<Integer>> ans, List<Integer> prev, int[] cands, int target, int curSum, int p) {
    if(curSum == target) {
      ans.add(new ArrayList(prev));
      return;
    }
    if(p >= cands.length) return;

    for(int i = p; i< cands.length; i++) {
      if((curSum + cands[i]) <= target) {
        prev.add(cands[i]);
        backTrackingHelper(ans, prev, cands, target, curSum + cands[i],i);
        prev.remove(prev.size() - 1);
      }
    }
  }
}
