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
 // Time: O(n)
 // Space: O(h)
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return validate(root->left, LLONG_MIN, root->val) && validate(root->right, root->val, LLONG_MAX);
    }

private:
    bool validate(TreeNode* node, long long min, long long max) {
        if(!node) return true;

        if(node->val <= min || node->val >= max) return false;

        return validate(node->left, min, node->val) && validate(node->right, node->val, max);
    }
};
