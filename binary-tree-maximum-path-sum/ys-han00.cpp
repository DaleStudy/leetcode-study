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
    int max_sum = INT_MIN;

    int dfs(TreeNode* node) {
        if(!node)
            return 0;
        
        int left_max = max(dfs(node->left), 0);
        int right_max = max(dfs(node->right), 0);
        
        max_sum = max(node->val + left_max + right_max, max_sum);
    
        return node->val + max(left_max, right_max);
    }

    int maxPathSum(TreeNode* root) {
        dfs(root);
        return max_sum;
    }
};

