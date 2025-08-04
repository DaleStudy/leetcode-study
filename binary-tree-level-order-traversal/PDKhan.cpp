class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;

        if(!root)
            return result;

        queue<TreeNode*> q;

        q.push(root);

        while(!q.empty()){
            int len = q.size();
            vector<int> level;

            for(int i = 0; i < len; i++){
                TreeNode* curr = q.front();
                q.pop();

                if(curr->left)
                    q.push(curr->left);
                
                if(curr->right)
                    q.push(curr->right);

                level.push_back(curr->val);
            }

            result.push_back(level);
        }

        return result;
    }
};
