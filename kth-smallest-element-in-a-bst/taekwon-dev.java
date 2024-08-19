/**
 *   사고의 흐름:
 *   - Binary Search Tree & 순서?
 *   - In-order 방식으로 순회를 해야겠다.
 *   - 1-indexed 이므로 리스트에 옮기고 k번째 접근한다면 -1 해서 접근해야겠다.
 *   - 근데, In-order 순회 어떻게 하더라? ㅋㅋ (재귀로 했던 것 같은데..) >> 여기서 검색 (...)
 *
 *   시간 복잡도: O(N)
 *   - BST 모든 노드를 다 순회해야 함
 *
 *   공간 복잡도: O(N)
 *   - 내가 활용한 스택을 기준으로 보면,
 *   - Stack 에 최대로 많이 들어갈 수 있는 수는 BST 높이
 *     - BST 는 최악의 경우 한 쪽으로 완전히 편향되어 높이가 N이 될 수도 있고,
 *     - 균형이 잘 맞다면 (마치 AVL, Red-Black) log N이 될 수 있음
 *     - 따라서 O(N) 이지만, 트리의 균형이 잘 맞다면 O(log N)
 */

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
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;
        int count = 0;

        while (current != null || !stack.isEmpty()) {
            while (current != null) {
                stack.push(current);
                current = current.left;
            }

            current = stack.pop();
            count++;

            if (count == k) {
                return current.val;
            }

            current = current.right;
        }

        return -1;
    }
}
