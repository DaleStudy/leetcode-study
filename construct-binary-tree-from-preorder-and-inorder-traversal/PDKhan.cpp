class Solution {
public:
    TreeNode* build(vector<int>& preorder, int& pos, vector<int>& inorder, int start, int end) {
        if(start >= end)
            return nullptr;

        int i;

        for(i = start; i < end; i++){
            if(preorder[pos] == inorder[i])
                break;
        }

        TreeNode* root = new TreeNode(preorder[pos]);

        pos++;

        root->left = build(preorder, pos, inorder, start, i);
        root->right = build(preorder, pos, inorder, i + 1, end);

        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int pos = 0;

        return build(preorder, pos, inorder, 0, inorder.size());
    }
};
