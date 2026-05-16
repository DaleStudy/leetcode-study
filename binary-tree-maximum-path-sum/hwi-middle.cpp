/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int ans = -1000;
        impl(root, ans);
        return ans;
    }

private:
    int impl(TreeNode* root, int& ans)
    {
        if (root == nullptr)
        {
            return 0;
        }

        // 왼쪽과 오른쪽 자식을 재귀적으로 순회
        int l = impl(root->left, ans);
        int r = impl(root->right, ans);
        int cur = root->val;

        // 최댓값 업데이트
        ans = max(ans, max(0, l) + max(0, r) + cur);

        // 부모에게 전달할 값
        // -> 재방문이 허용되지 않으므로 최댓값과는 다름
        return max(0, max(l, r) + cur);
    }
};
