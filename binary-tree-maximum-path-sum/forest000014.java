/*
# Time Complexity: O(n)
# Space Complexity: O(n)
  - 재귀 호출 내부에서 left, right 변수를 사용하고, 재귀 호출 최대 깊이는 n이므로
# Solution
전체 문제를 각 subtree에 대한 문제로 쪼개어 생각할 수 있습니다.
임의의 노드 x에 대해, x의 왼쪽 자식을 x_l, x의 오른쪽 자식을 x_r, x의 값을 x.val이라고 정의하겠습니다.
x를 root로 하는 subtree에서 'x를 path의 한쪽 끝으로 하는 path sum 중 최대값'을 dp[x]라고 정의하겠습니다.
그러면 dp[x] = max(max(0, dp[x_l]) + x.val, max(0, dp[x_r]) + x.val) 로 구할 수 있습니다. (subtree의 dp 값이 음수인 경우는 버리면 되기 때문에.)
이제 root로부터 출발해서 DFS로 전체 노드를 순회하며 이 점화식을 적용하면, 전체 tree에 대해 dp값을 구할 수 있습니다.
단, 문제에서 원하는 답은 root를 반드시 path의 한쪽 끝으로 원하는 것은 아니고, 심지어 root가 path에 포함되지 않아도 되기 때문에,
어중간한(?) (= root를 path에 포함하지 않는) path도 고려할 필요가 있는데요.
이를 고려하기 위해, 각 재귀 함수 호출마다 max(0, dp[x_l]) + root.val + max(0, dp[x_r]) 값이 정답이 될 수 있는지 체크하는 과정이 필요합니다.
*/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int ans = -30_000_001;
    public int maxPathSum(TreeNode root) {
        maxInTree(root);

        return ans;
    }

    public int maxInTree(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = Math.max(0, maxInTree(root.left));
        int right = Math.max(0, maxInTree(root.right));

        ans = Math.max(ans, left + root.val + right);

        return root.val + Math.max(left, right);
    }
}
