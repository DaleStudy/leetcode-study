/**
[문제풀이]
- 최대 depth 구하기
- left or right의 null일 때 depth의 max 구하기
- DFS 1
time: O(N), space: O(N)
    class Solution {
        public int maxDepth(TreeNode root) {
            return nextNode(root, 0);
        }

        private int nextNode(TreeNode node, int depth) {
            if (node == null) {
                return depth;
            }

            int leftDepth = nextNode(node.left, depth + 1);
            int rightDepth = nextNode(node.right, depth + 1);
            return Math.max(leftDepth, rightDepth);
        }
    }
- DFS 2
time: O(N), space: O(N)

[회고]
이전에 풀었던 Merget Two Sorted Lists 문제에서 주어진 메서드를 재사용할 수 있겠다는 생각으로 풀 수 있었다!
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
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);
        return Math.max(leftDepth, rightDepth) + 1;
    }
}

