/**
 *  https://www.algodale.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
 *
 *  <풀이1 기준> 시도!
 *  - 공간 복잡도: O(N^2) - Java 에서는 Call-by-value, 메서드 호출 시 인자 값이 복사되어 전달됨 / 배열 길이에 따라서 재귀 호출 스택이 점점 깊어짐 (각 호출마다 서브 배열 생성)
 *  - 시간 복잡도: inorder 배열에서 root 노드를 찾아가는 과정이 O(N), 그리고 이를 재귀 호출마다 반복하므로 O(N^2)
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return buildTree(preorder, inorder, 0, 0, inorder.length - 1);
    }

    private TreeNode buildTree(int[] preorder, int[] inorder, int rootIdx, int inorderStartIdx, int inorderEndIdx) {
        if (inorderStartIdx > inorderEndIdx) {
            return null;
        }

        int rootVal = preorder[rootIdx];
        TreeNode root = new TreeNode(rootVal);

        int rootIdxOnInorder = 0;
        for (int i = inorderStartIdx; i <= inorderEndIdx; i++) {
            if (inorder[i] == rootVal) {
                rootIdxOnInorder = i;
                break;
            }
        }

        int leftLength = rootIdxOnInorder - inorderStartIdx;

        root.left = buildTree(preorder, inorder, rootIdx + 1, inorderStartIdx, rootIdxOnInorder - 1);
        root.right = buildTree(preorder, inorder, rootIdx + 1 + leftLength, rootIdxOnInorder + 1, inorderEndIdx);

        return root;
    }
}
