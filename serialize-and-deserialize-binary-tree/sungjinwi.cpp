/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
    public:
    
        // Encodes a tree to a single string.
        string serialize(TreeNode* root) {
            queue<TreeNode*>    q;
            ostringstream out;
    
            out << "[";
            if (root)
                q.push(root);
            while (!q.empty()) {
                TreeNode*   node = q.front();
                if (node == nullptr) {
                    out << "null";
                }
                else {
                    out << node->val;
                    q.push(node->left);
                    q.push(node->right);
                }
                q.pop();
                out << ",";
            }
    
            string result = out.str();
            if (result.back() == ',')
                result.pop_back();
            result += "]";
    
            return result;
        }
    
        // Decodes your encoded data to tree.
        TreeNode* deserialize(string data) {
            if (data == "[]")
                return nullptr;
            string  s = data.substr(1, data.size() - 2);
            vector<string> tokens;
            string  token;
            stringstream ss(s);
    
            while (getline(ss, token, ','))
                tokens.push_back(token);
            
            TreeNode*   root = new TreeNode(stoi(tokens[0]));
            queue<TreeNode*>    q;
            q.push(root);
    
            int index = 1;
    
            while (!q.empty() && index < tokens.size()) {
                TreeNode* node = q.front();
                q.pop();
    
                if (tokens[index] != "null") {
                    node->left = new TreeNode(stoi(tokens[index]));
                    q.push(node->left);
                }
                index++;
    
                if (index < tokens.size() && tokens[index] != "null") {
                    node->right = new TreeNode(stoi(tokens[index]));
                    q.push(node->right);
                }
                index++;
            }
            return root;
        }
    };
    
    // Your Codec object will be instantiated and called as such:
    // Codec ser, deser;
    // TreeNode* ans = deser.deserialize(ser.serialize(root));
