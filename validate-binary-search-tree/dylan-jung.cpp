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
    bool dfs(TreeNode* root, long minVal, long maxVal) {
        if(!(minVal < root->val && root->val < maxVal)) return false;
        bool isValid = true;
        if(root->left) {
            isValid = isValid && dfs(root->left, minVal, min((long)root->val, maxVal));
        }
        if(root->right) {
            isValid = isValid && dfs(root->right, max((long)root->val, minVal), maxVal);
        }
        return isValid;
    }

    bool isValidBST(TreeNode* root) {
        return dfs(root, -(1l << 32), 1l << 32);
    }
};
