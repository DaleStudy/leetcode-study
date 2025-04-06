class Solution {
    public:
        bool search(TreeNode* root, long min, long max){
            if(root == NULL)
                return true;
    
            if(root->val <= min || root->val >= max)
                return false;
            
            return search(root->left, min, root->val) && search(root->right, root->val, max);
        }
    
        bool isValidBST(TreeNode* root) {
            return search(root, (long)INT_MIN-1, (long)INT_MAX+1);
        }
    };
