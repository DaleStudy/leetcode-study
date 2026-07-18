import java.util.*;

// TC: O(n)
// SC: O(h)
class Solution {
    public int maxDepth(TreeNode root) {
        return calMaxDepth(root);
    }

    // 현재까지 최대 깊이는 Math.max(왼쪽 서브노드 최대 깊이 , 오른쪽 서브노드 최대깊이) + 1
    private int calMaxDepth(TreeNode node) {
        if (node == null) return 0;
        return Math.max(calMaxDepth(node.left), calMaxDepth(node.right)) + 1;
    }
}
