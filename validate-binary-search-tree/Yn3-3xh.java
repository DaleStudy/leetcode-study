/*
[문제풀이]
- node의 왼쪽은 작아야 한다.
- node의 오른쪽은 커야 한다.
- 2^31 - 1 까지면 int
    - 범위는 long

- dfs로 풀자 (O)
time: O(N), space: O(N)

[회고]
!!! int 범위이지만 비교를 위해서는 더 큰 단위가 필요하므로 Long을 사용해야 한다 !!!

leftMaxVal, rightMinVal 네이밍은
왼쪽 노드는 root가 커야 해서 leftMaxVal,
오른쪽 노드는 root가 작아야 해서 rightMinVal로
조금 더 직관적으로 지어봤다. (조건문도 마찬가지)
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
    public boolean isValidBST(TreeNode root) {
        return dfs(root, Long.MAX_VALUE, Long.MIN_VALUE);
    }

    private boolean dfs(TreeNode node, long leftMaxVal, long rightMinVal) {
        if (node == null) {
            return true;
        }

        if (!(node.val < leftMaxVal) || !(node.val > rightMinVal)) {
            return false;
        }

        return dfs(node.left, node.val, rightMinVal) && dfs(node.right, leftMaxVal, node.val);
    }
}
