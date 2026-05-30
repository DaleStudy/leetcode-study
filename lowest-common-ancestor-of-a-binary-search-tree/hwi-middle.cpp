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
        // p와 q가 root 기준 왼쪽과 오른쪽에 나뉘어 존재하면 root가 LCA
        while ((root->val - p->val) * (long long)(root->val - q->val) > 0LL)
        {
            root = root->val > p->val ? root->left : root->right;
        }

        return root;
    }
};
