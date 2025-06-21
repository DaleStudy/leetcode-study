class Codec {
public:
    string serialize(TreeNode* root) {
        string res;
        dfs(root, res);
        return res;
    }

    TreeNode* deserialize(string data) {
        istringstream iss(data);
        return dfs(iss);
    }

private:
    void dfs(TreeNode* node, string& res) {
        if (!node) {
            res += "N,";
            return;
        }
        res += to_string(node->val) + ",";
        dfs(node->left, res);
        dfs(node->right, res);
    }

    TreeNode* dfs(istringstream& iss) {
        string val;
        getline(iss, val, ','); // ','를 기준으로 하나씩 읽음
        if (val == "N") return nullptr;

        TreeNode* node = new TreeNode(stoi(val));
        node->left = dfs(iss);
        node->right = dfs(iss);
        return node;
    }
};
