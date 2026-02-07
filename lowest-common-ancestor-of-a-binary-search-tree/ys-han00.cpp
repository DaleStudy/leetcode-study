/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* node = root;
        while(node) {
            if(p->val < node->val && q->val < node->val)
                node = node->left;
            else if(p->val > node->val && q->val > node->val)
                node = node->right;
            else
                return node;
        }
        return node;
    }

    // TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    //     if(p->val < root->val && q->val < root->val)
    //         return lowestCommonAncestor(root->left, p, q);
    //     if(p->val > root->val && q->val > root->val)
    //         return lowestCommonAncestor(root->right, p, q);
    //     return root;
    // }
};

