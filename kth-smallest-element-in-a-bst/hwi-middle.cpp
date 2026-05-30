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
    int kthSmallest(TreeNode* root, int k) {
        int cur = 0;
        return impl(root, k, cur);
    }

    int impl(TreeNode* root, int k, int& cur) {
        if (root == nullptr)
        {
            return -1;
        }

        int l = impl(root->left, k, cur);
        if (l != -1)
        {
            return l;
        }

        if (++cur == k)
        {
            return root->val;
        }
        
        int r = impl(root->right, k, cur);
        if (r != -1)
        {
            return r;
        }

        return -1;
    }
};
