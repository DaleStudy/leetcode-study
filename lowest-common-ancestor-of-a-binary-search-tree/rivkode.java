/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

/*
1. 문제 이해
공통 조상을 찾는데 최소의 공통 조상을 찾는다
즉 최대한 루트에서 멀리 떨어져있는 그리고 노드와는 가장 가까이 있는 공통 조상을 찾는다

2. 알고리즘
답지 참고
재귀

3. 느낀점

이진트리의 특정을 활용해야했다.
이진트리 이므로 왼쪽 노드는 반드시 루트보다 작고 오른쪽은 크다
이 특성을 사용해서 목표 트리노드까지 가야한다
재귀의 반환조건이 공통조상을 찾았을때이다 여기서 공통조상이 되려면 2개의 값이 루트보다 하나는 크고 하나는 작아야 한다
위 조건일때 공통조상을 가지므로 이 위치까지 루트가 내려와야 한다

다시 말해 이 위치를 찾기 위해 2개의 값을 비교해서 큰지 작은지를 판단하고 둘다 아니라면 공통조상이므로 반환하면 된다
이 방법을 생각하기 위해서는 이진 트리 특징을 활용해야했고 왼쪽과 오른쪽 노드의 값을 비교해서 공통 조상 노드까지 내려온다는 생각을 했어야 했다


*/

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // 2개의 값이 루트 값 보다 작다면 왼쪽 서브트리를 확인
        if (p.val < root.val && q.val < root.val) {
            return lowestCommonAncestor(root.left, p, q);
        // 2개의 값이 루트 값 보다 크다면 오른쪽 서브트리를 확인
        } else if (p.val > root.val && q.val > root.val) {
            return lowestCommonAncestor(root.right, p, q);
        // 2개의 값 중 하나는 루트 값 보다 크고 하나는 작다면 현재 루트가 최소 공통 조상이므로 반환
        } else {
            return root;
        }
    }
}

