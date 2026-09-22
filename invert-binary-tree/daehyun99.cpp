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
    // Time: O(N)
    // Space: O(H) // H: height of hte tree
    TreeNode* invertTree(TreeNode* root) {
        return dfs(root);
        
    }

private:
    TreeNode* dfs(TreeNode* node) {
        if (node != nullptr) {
            TreeNode* temp = dfs(node->right);
            node->right = dfs(node->left);
            node->left = temp;
        }
        return node;
    }
};
