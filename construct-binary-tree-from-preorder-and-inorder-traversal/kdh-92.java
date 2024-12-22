/**
 * 특이사항
 * TreeNode 이해 & right 설정 부분 이해 필요
 * - 재귀 호출 형태로 if 조건 추가 (preStart > preorder.length -1 || inStart > inEnd) 일 경우엔 null 반환
 * - null일 때 상황 테스트하며 좀 더 살펴보기
 *
 * - right
 *   - preStart : preStart + inIdx - inStart + 1 (left 동일하게 preStart + 1에서 inIdx - inStart 를 추가해서 오른쪽 영역 탐색)
 */

class Solution {
    public static TreeNode buildTree(int[] preorder, int[] inorder) {
        // (1) helper 메소드를 재귀호출 사용
        // 시간복잡도 : O(N^2), 공간복잡도 : O(N)
        
        return helper(0, 0, inorder.length - 1, preorder, inorder);
    }

    public static TreeNode helper(int preStart, int inStart, int inEnd, int[] preorder, int[] inorder) {
        if (preStart > preorder.length - 1 || inStart > inEnd) return null;
        TreeNode node = new TreeNode(preorder[preStart]);
        int inIdx = 0;

        for (int i = inStart; i <= inEnd; i++) {
            if (node.val == inorder[i]) {
                inIdx = i;
                break;
            }
        }

        node.left = helper(preStart + 1, inStart, inIdx - 1, preorder, inorder);
        node.right = helper(preStart + inIdx - inStart + 1, inIdx + 1, inEnd, preorder, inorder);

        return node;
    }
}
