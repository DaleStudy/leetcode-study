// 중위 순회로 맨아래까지 내려가서 순서를 찾는다.
// 시간 복잡도를 유지하면서 탐색할 방법을 몰라서 GPT로 찾아봤음.
// 한번만 탐색하므로 시간복잡도는 O(N)
class Solution {
    int count = 0;
    int result = 0;

    public int kthSmallest(TreeNode root, int k) {
        inorder(root, k);
        return result;
    }

    private void inorder(TreeNode node, int k) {
        if (node == null) return;
        
        inorder(node.left, k);

        count++;
        if (count == k) {
            result = node.val;
            return;
        }

        inorder(node.right, k);
    }
}
