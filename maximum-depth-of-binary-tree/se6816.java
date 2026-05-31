/**
    DFS를 이용하여, 최대 깊이를 구하는 방식
    트리 노드의 개수 -> N
    시간 복잡도 : O(N)
    공간 복잡도 : O(log N)
 */
class Solution {
    public int maxDepth(TreeNode root) {
        return calculateDepth(root, 0);
    }

    public int calculateDepth(TreeNode node, int depth) {
        if(node == null) {
            return depth;
        }

        return Math.max(calculateDepth(node.left, depth + 1), calculateDepth(node.right, depth + 1));
    }
}
