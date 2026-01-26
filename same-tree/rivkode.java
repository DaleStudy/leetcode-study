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
루트노드를 입력받아서 모든 노드들이 서로 동일한지 체크

2. 알고리즘
bfs 사용 ?
queue 사용해서 각 레벨별로 동일한지 체크 ?

3. 예외

4. 구현
각 트리별로 queue 를 생성
최초 루트 노드 각 큐별로 넣기
while loop 시작
1. 


*/

import java.util.*;

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }

        if (p == null || q == null) {
            return false; // 둘중 하나만 false 이므로 서로 다름
        }

        if (p.val != q.val) {
            return false; // 서로 동일한 형태일때 값이 다르면 다르므로
        }

        return this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right); // 재귀 호출


        // Queue<Integer> pQueue = new LinkedList<>();
        // Queue<Integer> qQueue = new LinkedList<>();

        // pQueue.offer(p);
        // qQueue.offer(q);

        // while (pQueue.size() != 0 || qQueue.size() != 0) {
        //     TreeNode pNode = pQueue.poll();
        //     TreeNode qNode = qQueue.poll();

        //     pNode.left;
        // }
    }

    public boolean checkLeaf(TreeNode a, TreeNode b) {
        if (a == b) {
            return true;
        } else {
            return false;
        }
    }
}
