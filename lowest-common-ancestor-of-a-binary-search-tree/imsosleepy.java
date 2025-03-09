// 백트래킹으로 만들려다 while문으로 전환
// 문제만 봐선 아래에서 위로 가는 것 같지만, 이진 트리의 특성 상 루트보다 작으면 왼쪽, 크면 오른쪽으로 가면서
// 주어 진 수인 p,q 를 찾을 수 있다. p가 q보다 클 수 도 있다. 
// 한번만 순회하므로 O(N)
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        while (root != null) {
            if (root.val > p.val && root.val > q.val) {
                root = root.left;  // 왼쪽으로 이동
            } else if (root.val < p.val && root.val < q.val) {
                root = root.right; // 오른쪽으로 이동
            } else {
                return root;
            }
        }
        return null;
    }
}
