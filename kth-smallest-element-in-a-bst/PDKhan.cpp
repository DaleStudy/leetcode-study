class Solution {
public:
    void search(TreeNode* root, int k, int& cnt, int& result){
        if(root == NULL)
            return;
        if(cnt > k)
            return;
        
        search(root->left, k, cnt, result);

        cnt++;

        if(cnt == k)
            result = root->val;

        search(root->right, k, cnt, result);
    }

    int kthSmallest(TreeNode* root, int k) {
        int cnt = 0;
        int result = 0;

        search(root, k, cnt, result);

        return result;
    }
};
