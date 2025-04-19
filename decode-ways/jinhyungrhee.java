import java.util.*;
class Solution {

    public List<Integer> nums;
    public int numDecodings(String s) {
        nums = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            nums.add(s.charAt(i) - 48);
        }

        int[] memo = new int[nums.size() + 1];
        Arrays.fill(memo, -1);
        return dfs(0, memo);
    }

    public int dfs(int start, int[] memo) {

        if (start == nums.size()) return 1;

        if (memo[start] != -1) {
            return memo[start];
        }
        if (nums.get(start) == 0) {
            memo[start] = 0;
        }
        else if (start + 1 < nums.size() && nums.get(start) * 10 + nums.get(start + 1) < 27) {
            memo[start] = dfs(start + 1, memo) + dfs(start + 2, memo);
        } else {
            memo[start] = dfs(start + 1, memo);
        }
        return memo[start];
    }
}
