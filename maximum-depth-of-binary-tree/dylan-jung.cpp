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
    int dfs(TreeNode* root, int depth) {
        int ret = depth;
        if(root->left) ret = max(ret, dfs(root->left, depth+1));
        if(root->right) ret = max(ret, dfs(root->right, depth+1));
        return ret;
    }

    int maxDepth(TreeNode* root) {
        if(!root) return 0;
        return dfs(root, 1);
    }
};
