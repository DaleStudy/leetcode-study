/**
[문제풀이]
- target 숫자를 주어진 배열로 나눠보면서 0이 되는 것들을 고르면 되지 않을까?
- dfs로 풀어보자.
time: O(2^N), space: O(N);

[회고]
!!! dfs에서 기존 리스트가 이후에 변경될 수 있으므로 새 객체를 생성해서 넣어줘야 한다. !!!

DP로도 풀어보려고 했지만, 솔루션을 봐도 내가 풀 수 없을 것 같았다..
 */
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> results = new ArrayList<>();
        dfs(candidates, target, 0, results, new ArrayList<>(), 0);
        return results;
    }

    private void dfs(int[] candidates, int target, int index, List<List<Integer>> results, List<Integer> result, int sum) {
        if (sum == target) {
            results.add(new ArrayList<>(result));
            return;
        }

        if (sum > target || index >= candidates.length) {
            return;
        }

        int num = candidates[index];
        result.add(num);
        dfs(candidates, target, index, results, result, sum + num);

        result.remove(result.size() - 1);
        dfs(candidates, target, index + 1, results, result, sum);
    }
}

