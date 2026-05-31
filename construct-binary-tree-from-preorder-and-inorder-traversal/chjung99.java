import java.util.HashMap;
import java.util.Map;

class Solution {
    // 빠른 조회를 위해 inorder의 값과 인덱스를 저장할 Map
    private Map<Integer, Integer> inMap;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        inMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inMap.put(inorder[i], i);
        }

        return construct(preorder, 0, preorder.length - 1, 0, inorder.length - 1);
    }

    private TreeNode construct(int[] preorder, int preStart, int preEnd, int inStart, int inEnd) {
        // 기저 조건: 더 이상 처리할 노드가 없는 경우
        if (preStart > preEnd || inStart > inEnd) {
            return null;
        }

        // 1. preorder의 현재 구간 첫 번째 원소가 루트 노드입니다.
        int rootVal = preorder[preStart];
        TreeNode root = new TreeNode(rootVal);

        // 2. inorder에서 루트의 위치를 찾아 왼쪽/오른쪽 서브트리 범위를 나눕니다.
        int rootIdx = inMap.get(rootVal);
        int leftSize = rootIdx - inStart; // 왼쪽 서브트리에 포함된 노드 개수

        // 3. 재귀적으로 왼쪽 자식 노드들을 연결합니다.
        // preorder 범위: 루트 다음(preStart + 1)부터 개수(leftSize)만큼
        // inorder 범위: 원래 시작점부터 루트 앞(rootIdx - 1)까지
        root.left = construct(preorder, preStart + 1, preStart + leftSize,
                inStart, rootIdx - 1);

        // 4. 재귀적으로 오른쪽 자식 노드들을 연결합니다.
        // preorder 범위: 왼쪽 식구들 끝난 지점 다음(preStart + leftSize + 1)부터 끝까지
        // inorder 범위: 루트 다음(rootIdx + 1)부터 끝까지
        root.right = construct(preorder, preStart + leftSize + 1, preEnd,
                rootIdx + 1, inEnd);

        return root;
    }
}


