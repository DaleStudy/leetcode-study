// 혼자서 못풀어서 GPT의 도움을 받음
// 왜 두 배열이 필요한가?
// 전위 순회(preorder): 트리의 루트를 가장 먼저 방문합니다. 그 후 왼쪽 서브트리, 오른쪽 서브트리를 방문합니다. 하지만 이 정보만으로는 각 서브트리가 어느 부분인지, 그리고 그 서브트리의 구체적인 구성 요소가 무엇인지를 알 수 없습니다.
// 
// 중위 순회(inorder): 트리의 왼쪽 서브트리를 먼저 방문하고, 루트를 방문한 후, 오른쪽 서브트리를 방문합니다. 이 배열을 통해 루트가 트리의 어느 위치에 있는지 확인할 수 있습니다. 루트의 위치를 알면, 그 위치를 기준으로 왼쪽과 오른쪽 서브트리를 나눌 수 있습니다.

// 한 배열로는 트리의 구조를 복원할 수 없는 이유
// 전위 순회만으로는 각 노드의 왼쪽 자식인지 오른쪽 자식인지 알 수 없습니다. 예를 들어, [3, 9, 20, 15, 7]라는 전위 순회 배열만 있다면, '9'가 3의 왼쪽 자식인지 오른쪽 자식인지 알 수 없습니다.
// 중위 순회만으로도 트리의 루트를 알 수 없으므로, 각 서브트리의 구체적인 구조를 알 수 없습니다.
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return buildTreeHelper(preorder, inorder, 0, 0, inorder.length - 1);
    }

    private TreeNode buildTreeHelper(int[] preorder, int[] inorder, int preStart, int inStart, int inEnd) {
        if (inStart > inEnd) return null;

        int rootVal = preorder[preStart];
        TreeNode root = new TreeNode(rootVal);

        int rootIndex = -1;
        for (int i = inStart; i <= inEnd; i++) {
            if (inorder[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }

        int leftSize = rootIndex - inStart;
        root.left = buildTreeHelper(preorder, inorder, preStart + 1, inStart, rootIndex - 1);
        root.right = buildTreeHelper(preorder, inorder, preStart + leftSize + 1, rootIndex + 1, inEnd);

        return root;
    }

}
