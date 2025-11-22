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

/*
1. 문제 이해

트리가 주어졌을 때 해당 트리가 BST인지 판별
BST인제 판별하는 방법은 key 기준 left는 작아야 하고 right는 커야 한다.
이 조건이 실패하면 해당 트리는 BST가 아니다.

2. 예외 케이스

노드 개수의 범위는
tree node가 1개부터 최고 1만개 까지

1개일 경우
바로 반환

그 외는 계산 진행


3. 알고리즘 선택

dfs 선택
a. 노드 key 기준으로 계속 파고들어서 반복할 수 있을 것 같아서
b. left, right가 있는지를 기준으로 있다면 다시 dfs가 가능해서

bfs로 해도 key를 알고 있으니까 되긴 할 것 같은데 일단 dfs로 해보자

아니다 bfs로 해야할 것 같은데 ? 이게 깊게 들어가는게 중요한게 아니라 전체 탐색을 해야하니 순차적으로 key들을 탐색하면서 작은지 큰지를 판별하면 될 것 같다.

bfs로 진행해보자

아니다 .. dfs가 맞네 하한 상한을 정해줘야 함
그리고 예외 케이스 있다 [-2147483648,null,2147483647]

처음에 하한과 상한을 MIN_VALUE, MAX_VALUE를 통해 사용하고 있었는데 위 엣지 케이스를 발견

처음에는 Integer.MIN_VALUE 와 같이 Integer을 사용해서 위 예외 케이스를 만났는데
이걸 15분 동안 고민하다 gemini 한테 물어보니까 그냥 Long 쓰면 된단다 ...
Long으로 변경하니 통과 ..

만약 조건범위가 Long 의 범위였다면 ,,? 어떻게 해결해야했을까.
4. 구현

*/

import java.util.*;

class Solution {
    public boolean isValidBST(TreeNode root) {
        Long min = Long.MIN_VALUE;
        Long max = Long.MAX_VALUE;

        if (root.left == null && root.right == null) {
            return true;
        }

        return dfs(root, min, max);

    }

    public boolean dfs(TreeNode node, long min, long max) {
        if (node == null) {
            return true;
        }

        // 정상 범위
        if (min < node.val && node.val < max) {
            return dfs(node.left, min, node.val) && dfs(node.right, node.val, max);
        } else {
            return false;
        }
    }

    // 아래와 같이 풀려고 했으나 하한값과 상한값에 대한 인자를 넘겨줘야 하는데 넘겨줄 수 없어서 dfs로 풀어야 함
    // 에러 케이스
    // [5,4,6,null,null,3,7]
    // private static int preKey;
    // public boolean isValidBST(TreeNode root) {
    //     Queue<TreeNode> queue = new LinkedList<>();
        
    //     queue.offer(root);
    //     preKey = root.val;

    //     while (!queue.isEmpty()) {
    //         TreeNode node = queue.poll();
    //         int key = node.val;
    //         TreeNode left = node.left;
    //         TreeNode right = node.right;

    //         // left 처리
    //         if (left != null) {
    //             queue.offer(left);
    //             if (left.val >= key) {
    //                 return false;
    //             }

    //             if ()
    //         }

    //         // right 처리
    //         if (right != null) {
    //             queue.offer(right);
    //             if (right.val <= key) {
    //                 return false;
    //             }
    //         }
    //     }

    //     return true;
    // }
}

