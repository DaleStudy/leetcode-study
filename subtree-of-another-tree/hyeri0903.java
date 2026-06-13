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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        /**
        1.root 트리의 subtree가 subRoot tree 이면 true 아니면 false return
        2.constraints
        - subRoot tree 가 존재하는데 거기에 자식 노드가 추가로 있으면 안됨
        - 자기 자신 root tree = subRoot tree 일수도 있음
        3.solution
        - 재귀함수로 subTree 찾고 subRoot 의 트리와 동일한지 검사
        - root 트리 노드 수 : n, subRoot 트리 노드 수 : m
        - timeComplexity : O(nm)
         */
         if(root == null) return false;

         //먼저 트리가 동일한지 체크 -> left subTree check -> right subTree check
         return isSameTree(root, subRoot)
         || isSubtree(root.left, subRoot)
         || isSubtree(root.right, subRoot);

    }
    private boolean isSameTree(TreeNode a, TreeNode b) {
        //둘 다 null
        if (a == null && b == null) return true;
        //둘중 하나만 null
        if (a == null || b == null) return false;
        //값이 다른 경우
        if(a.val != b.val) return false;
        //현재 값이 다르면 왼쪽끼리, 오른쪽끼리 비교, 모두 같아야 true return
        return isSameTree(a.left, b.left) && isSameTree(a.right, b.right);
    }
}
