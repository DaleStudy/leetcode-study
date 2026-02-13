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
    vector<vector<int>> ans;
    void rec(TreeNode* curr, int level) {
        if(ans.size() < level)
            ans.push_back(vector<int>());
        ans[level - 1].push_back(curr->val);
        if(curr->left)
            rec(curr->left, level + 1);
        if(curr->right)
            rec(curr->right, level + 1);
    }
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(root)
            rec(root, 1);
        return ans;
    }
};

