// 트리의 형태를 바꾸는건 대부분 DFS로 푸는게 공간복잡도 측면에서 유리하다.
// BFS로도 풀이 가능하지만, BFS는 대부분 큐를 이용해서 공간복잡도가 높아진다.
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        
        TreeNode temp = root.left;
        root.left = invertTree(root.right);
        root.right = invertTree(temp);

        return root;
    }
}
