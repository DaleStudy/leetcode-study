/**
 * 이진 트리의 최대 깊이를 재귀적으로 계산 (DFS)
 * 
 * 시간 복잡도: O(n), n은 트리의 노드 수
 * 공간 복잡도: O(h), h는 트리의 높이, 재귀 호출로 인해 스택에 쌓이는 함수 호출의 깊이 때문
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);

        return Math.max(leftDepth, rightDepth) + 1;
    }
}

/**
 * 이진 트리의 최대 깊이를 반복적으로 계산 (BFS)
 * 
 * 시간 복잡도: O(n), n은 트리의 노드 수
 * 공간 복잡도: O(n), 큐에 저장되는 노드 수 때문
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        int depth = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                TreeNode current = queue.poll();

                if (current.left != null) {
                    queue.offer(current.left);
                }

                if (current.right != null) {
                    queue.offer(current.right);
                }
            }

            depth++;
        }

        return depth;
    }
}
