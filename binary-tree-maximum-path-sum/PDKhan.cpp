class Solution {
    public:
        int dfs(TreeNode* root, int& result){
            if(root == nullptr)
                return 0;
            
            int left = max(0, dfs(root->left, result));
            int right = max(0, dfs(root->right, result));
            int sum = root->val + left + right;
    
            result = max(result, sum);
    
            return root->val + max(left, right);
        }
    
        int maxPathSum(TreeNode* root) {
            int result = INT_MIN;
    
            dfs(root, result);
            return result;
        }
    };
