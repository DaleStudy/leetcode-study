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

/**
 runtime : 2ms
 memory : 45.13mb
 */

// [idea] 재귀적 DFS로 left 먼저 끝까지 가고 null을 만나면 backtrack
//        재귀적 DFS로 right 노드 끝까지 방문하고 null 만나면 backtrack
//        방문 노드 저장(혹은 출력) 순서에 따라서 '전위(pre-order)', '중위(in-order)', '후위(post-order)'가 결정됨

// [time-complexity] : O(N) -> 모든 트리의 노드를 한번씩 방문
/**
 모든 이진 트리 탐색이 O(2^N)은 아니다!
 1.모든 노드를 '한 번씩만' 방문하는 경우 -> O(N)
 2.모든 경로를 '선택지로 분기'하는 경우 -> O(2^N)
 - 백트래킹 / 부분집합 / 순열 / 이진결정트리 와 같은 문제
 - 한 노드에서 2개의 선택지가 계속 발생하므로 O(2^N)
 - *트리 탐색이 아닌 '조합/경우의 수 문제'의 시간복잡도*
 */

// [space-complexity] : O(N) -> OrderedList에 N개의 값 저장

import java.util.*;
class Solution {

    List<Integer> orderedList = new ArrayList<>();

    public boolean isValidBST(TreeNode root) {

        dfs(root);
        // iterativeDFS(root);

        if (orderedList.isEmpty()) return false;
        for (int i = 0; i < orderedList.size() - 1; i++) {
            if (orderedList.get(i) >= orderedList.get(i + 1)) return false;
        }
        return true;

    }

    // root 노드 '방문 순서' 기준
    // root 노드를 '먼저 방문'하면 '전위'(pre-order) : 루트 → 왼쪽 → 오른쪽
    // root 노드를 '중간에 방문'하면 '중위' (in-order) : 왼쪽 -> 루트 -> 오른쪽
    // root 노드를 '마지막에 방문'하면 '후위' (post-order) : 왼쪽 -> 오른쪽 -> 루트
    public void dfs(TreeNode node) {
        if (node == null) return;

        if (node.left != null) dfs(node.left);
        // 저장 위치를 어디에 두느냐에 따라 순회 방식이 결정
        orderedList.add(node.val); // in-order (중위 순회 방식)
        if (node.right != null) dfs(node.right);

    }


    /**
     runtime : 9ms
     memory : 45.41mb
     */

    // [idea] : 오른쪽 sub-tree로 이동하며 아래의 1-2-3 과정 반복 수행
    // [time-complexity] : O(N)
    // [space-complexity] : O(N)

    public void iterativeDFS(TreeNode root) {

        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode current = root;
        while (current != null || !stack.isEmpty()) {

            // 1. 왼쪽의 모든 노드를 계속해서 stack에 push
            while (current != null) {
                stack.push(current);
                current = current.left;
            }
            // 2. 왼쪽 노드 끝에 도달하면 스택에서 꺼내서 방문
            current = stack.pop();
            orderedList.add(current.val);
            // 3. 오른쪽 노드로 이동
            current = current.right;
        }
    }
}
