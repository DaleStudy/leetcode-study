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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        /**
        1.problem: 2개의 bst 가 동일한지 체크
        2.constraints - 구조와 노드가 동일해야된다
        3.solution - DFS
        1) 두 트리의 노드가 모두 null -> true
        2) 둘중 하나만 null -> false
        3) 값이 다르면 false
        4)재귀로 트리의 구조가 동일한지 체크
         */

         if(p == null && q == null) {
            return true;
         }
         if(p == null || q == null) {
            return false;
         }
        if(p.val != q.val) {
            return false;
        }

        if(isSameTree(p.left, q.left) && isSameTree(p.right, q.right)) {
            return true;
        }
        return false;
    }

}
