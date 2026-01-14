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
    TreeNode* invertTree(TreeNode* root) {
        queue<TreeNode*> que;
        que.push(root);

        while(!que.empty()) {
            TreeNode *curr = que.front();
            que.pop();

            if(!curr)
                continue;
            
            swap(curr->left, curr->right);
            que.push(curr->left);
            que.push(curr->right);
        }

        return root;
    }
};

