class Solution {
public:
    bool compare_tree(TreeNode* root, TreeNode* subRoot) {
        if(!root && !subRoot)
            return true;
        else if(!root || !subRoot || root->val != subRoot->val)
            return false;
        
        return compare_tree(root->left, subRoot->left) && compare_tree(root->right, subRoot->right);
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(!root)
            return false;
        
        if(compare_tree(root, subRoot))
            return true;

        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
};
