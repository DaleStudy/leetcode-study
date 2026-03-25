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
    bool isValidBST(TreeNode* root) {
        vector<int> v;
        v.reserve(1e4);
        
        solve(root, v);

        int len = v.size();
        for (int i = 0; i < len - 1; ++i)
        {
            if (v[i] >= v[i + 1])
            {
                return false;
            }
        }

        return true;
    }

    void solve(TreeNode* root, vector<int>& v)
    {
        if (root->left != nullptr)
        {
            solve(root->left, v);
        }

        v.push_back(root->val);

        if (root->right != nullptr)
        {
            solve(root->right, v);
        }
    }
};
