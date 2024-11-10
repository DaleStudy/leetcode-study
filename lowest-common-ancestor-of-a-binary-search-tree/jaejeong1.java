
//  Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}


class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // 플이: p,q 둘다 root 보다 값이 적으면 왼쪽 서브트리를, 둘다 크면 오른쪽 서브트리를 탐색해야한다.
        // 그렇지 않으면 해당 root가 최저 공통 조상이 된다.
        // TC: O(H), H: 트리의 높이
        // SC: O(1)
        var node = root;
        while (node != null) {
            if (p.val < node.val && q.val < node.val) {
                node = node.left;
            } else if (p.val > node.val && q.val > node.val) {
                node = node.right;
            } else {
                break;
            }
        }

        return node;
    }
}
