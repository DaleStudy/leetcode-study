// TC: O(n)
//   - 노드의 개수만큼 dfs 순회
// SC: O(h)
//   - 재귀 스택은 트리의 높이(h)만큼 쌓임
//   - 최악: 치우친 트리인 경우, O(n)
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        // node->val의 범위가 int 전체 범위를 쓰므로, 하한 및 상한을 long 타입의 범위로 지정
        return dfs(root, LONG_MIN, LONG_MAX);
    }

    bool dfs(TreeNode* node, long lower, long upper) {
        if (!node) return true;

        // node의 val이 하한, 상한 사이에 있지 않으면 false로 return
        if (!(lower < node->val && node->val < upper)) return false;

        // node의 왼쪽 자식 탐색 시, node의 val을 상한으로 설정해서 재귀
        // node의 오른쪽 자식 탐색 시, node의 val을 하한으로 설정해서 재귀
        // 두 재귀함수의 결과를 and 연산하여 return (하나라도 false면 전체가 false)
        return dfs(node->left, lower, node->val) && dfs(node->right, node->val, upper);
    }
};
