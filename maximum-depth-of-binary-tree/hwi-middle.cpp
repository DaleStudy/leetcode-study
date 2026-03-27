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
    int maxDepth(TreeNode* root) {
        return solve(root, 0);
    }

    int solve(TreeNode* root, int depth)
    {
        if (root == nullptr)
        {
            return depth;
        }

        int l = solve(root->left, depth);
        int r = solve(root->right, depth);

        return max(l, r) + 1;
    }
};
