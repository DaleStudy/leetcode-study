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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> v;
        if (root == nullptr)
        {
            return v;
        }
        
        // BFS로 해결
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        while (!q.empty())
        {
            TreeNode* cur;
            int h;
            tie(cur, h) = q.front();
            q.pop();

            if (v.size() == h)
            {
                v.push_back(vector<int>());
            }

            v[h].push_back(cur->val);

            if (cur->left != nullptr)
            {
                q.push({cur->left, h + 1});
            }

            if (cur->right != nullptr)
            {
                q.push({cur->right, h + 1});
            }
        }

        return v;
    }
};
