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
 * 처음에는 가장 아래의 코드와 같이 BFS 로 접근해서 풀려고 했었지만 알고리즘 선택이 잘못되었음을 깨달았다.
 * 처음 BFS 로 접근했던 이유는 노드의 값이 동일한 경우를 찾았을 때 그때부터 트리를 순회하면서 서로 비교하면 될 줄 알았다.
 * 하지만 이렇게 문제를 풀려고 하니 여러 엣지 케이스들을 놓쳤었다. [1] [0] / [1] [1] 등등
 * 그리고 같은 노드의 값을 찾았다 한들 찾았을 때 다시 DFS로 접근하는? 너무 복잡한 방식을 택했다. 너무 돌아갔다. (이때 뭔가 잘못되었음을 느꼈다.)
 * 
 * 처음부터 DFS를 선택했어야 했고 문제 특성상 조건들이 재귀적으로 정의가 되었다. A B 가 동일한가 ? / A 왼쪽 서브트리가 B를 포함하는가 ? / A 오른쪽 서브트리가 B 를 포함하는가 ?
 * 여기서 비교하려는 2개의 노드를 두고 똑같은 포인트를 탐색하며 실제 사람인 내가 비교하려는 것 처럼 비교하는것이 아니었다.
 * 포인트는 문제처럼 root가 subRoot를 서브트리로 포함하는가 ? 이다.
 * 이걸 3가지 포인트로 나누어서 root 와 subRoot가 그 자체로 동일한가 ? / root.left와 SubRoot , root.right 와 subRoot가 동일한가를 보는 것이었다.
 * 그리고 여기서 재귀를 사용해서 값을 체크하는 것이 포인트였다.
 * BFS와 DFS를 잘 이해하고 사용하자.
 */

import java.util.*;

class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // subRoot 가 null 이면 true를 반환한다. 왜냐하면 모든 노드들은 자식노드로 null 을 가질 수 있기 때문이다.
        if (subRoot == null) {
            return true;
        }
        
        // subRoot 가 null 이 아닌데 root 만 null 이면 이 둘의 노드는 다르다는 의미이다.
        if (root == null) {
            return false;
        }

        // 위 2개의 null 체크를 하고 root와 subRoot 가 서로 동일한지 체크한다.
        if (isSameTree(root, subRoot)) {
            return true;
        }

        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    public boolean isSameTree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) {
            return true; // 2개의 노드 value 가 모두 null 이면 true 반환
        }

        if (root == null || subRoot == null || root.val != subRoot.val) {
            return false; // 2개중 하나만 Null 이거나 2개의 노드 값이 다를 경우 false 반환
        }

        // 위 2개의 상황이 아니면 모두 같은 값을 가진 노드들의 값이 같다는 의미이므로 재귀적으로 자식들을 체크
        return isSameTree(root.left, subRoot.left) && isSameTree(root.right, subRoot.right);
    }
}

// import java.util.*;

// class Solution {
//     static boolean result;
//     public boolean isSubtree(TreeNode root, TreeNode subRoot) {
//         result = true;

//         Queue<TreeNode> queue = new LinkedList<>();
//         queue.offer(root);
//         int subRootValue = subRoot.val;
//         if (root == null && subRoot == null) {
//             return true;
//         }

//         if (root.left == null && root.right == null && subRoot.left == null && subRoot.right == null) {
//             if (root.val == subRootValue) {
//                 return true;
//             } else {
//                 return false;
//             }
//         }

//         while (!queue.isEmpty()) {
//             TreeNode qRoot = queue.poll();
//             if (qRoot.val == subRootValue) {
//                 result = checkEqual(qRoot, subRoot);
//                 break;
//             }

//             if (qRoot.left != null) {
//                 if (qRoot.left.val == subRootValue) {
//                     result = checkEqual(qRoot.left, subRoot);
//                     break;
//                 }
//                 queue.offer(qRoot.left);
//             }

//             if (qRoot.right != null) {
//                 if (qRoot.right.val == subRootValue) {
//                     result = checkEqual(qRoot.right, subRoot);
//                     break;
//                 }
//                 queue.offer(qRoot.right);
//             }
//         }

//         return result;
//     }

//     public boolean checkEqual(TreeNode root, TreeNode subRoot) {
//         if (root == null && subRoot == null) {
//             return true; // 2개의 노드 value 가 모두 null 이면 true 반환
//         }

//         if (root == null || subRoot == null || root.val != subRoot.val) {
//             return false; // 2개중 하나만 Null 이거나 2개의 노드 값이 다를 경우 false 반환
//         }

//         // 위 2개의 상황이 아니면 모두 같은 값을 가진 노드들의 값이 같다는 의미이므로 재귀적으로 자식들을 체크

//         return checkEqual(root.left, subRoot.left) && checkEqual(root.right, subRoot.right);
//     }
// }

