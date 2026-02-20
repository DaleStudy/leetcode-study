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
    unordered_map<int, int> indices;
    int pre_idx = 0;
    
    TreeNode* dfs(const vector<int>& preorder, int start, int end) {
        if (start > end)
            return nullptr;

        int root_val = preorder[pre_idx++];
        TreeNode* root = new TreeNode(root_val);

        int mid = indices[root_val];

        root->left = dfs(preorder, start, mid - 1);
        root->right = dfs(preorder, mid + 1, end);

        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for (int i = 0; i < inorder.size(); ++i)
            indices[inorder[i]] = i;
        
        pre_idx = 0;

        return dfs(preorder, 0, inorder.size() - 1);
    }
};
