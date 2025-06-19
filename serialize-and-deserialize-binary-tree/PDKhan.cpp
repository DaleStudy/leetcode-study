class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string result;

        if(root == nullptr)
            return result;

        queue<TreeNode*> q;

        q.push(root);

        while(!q.empty()){
            TreeNode* curr = q.front();

            q.pop();

            if(curr){
                result += to_string(curr->val) + ",";
                q.push(curr->left);
                q.push(curr->right);
            }else{
                result += "NULL,";
            }
        }

        return result;
    }
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if(!data.size())
            return nullptr;
        
        queue<TreeNode*> q;
        vector<string> values;
        size_t prev = 0;
        size_t pos = data.find(",", prev);

        while(pos != string::npos){
            values.push_back(data.substr(prev, pos - prev));
            prev = pos + 1;
            pos = data.find(",", prev);
        }

        int idx = 0;
        TreeNode* root = new TreeNode(stoi(values[idx++]));
        q.push(root);

        while(!q.empty()){
            int left = idx++;
            int right = idx++;
            TreeNode* curr = q.front();
            q.pop();

            if(left < values.size() && values[left] != "NULL"){
                curr->left = new TreeNode(stoi(values[left]));
                q.push(curr->left);
            }
            
            if(right < values.size() && values[right] != "NULL"){
                curr->right = new TreeNode(stoi(values[right]));
                q.push(curr->right);
            }
        }

        return root;
    }
};
